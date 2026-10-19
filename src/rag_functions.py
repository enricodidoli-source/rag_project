import uuid
import math
import numpy as np
from numpy.linalg import norm
import optuna

from transformers import pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_classic.schema import Document

from langchain_huggingface import HuggingFacePipeline
from langchain_classic.chains import RetrievalQA




def semantic_similarity(text1, text2, embedding_model):
    """Computes how similar are two texts
    input: - Sentence1
           - Sentence2
           - Embedding model"""

    v1 = embedding_model.embed_query(text1)
    v2 = embedding_model.embed_query(text2)

    # Cosine Similarity
    sim = np.dot(v1, v2) / (norm(v1) * norm(v2))
    return sim
    
def run_trial(param_dict, full_text, embedding_model, QA_CHAIN_PROMPT, training_set, base_model, tokenizer, phase = 'training', q_hat = None):

        # set the text splitter
        text_splitter = RecursiveCharacterTextSplitter(
                chunk_size  = param_dict['chunk_size'],
                chunk_overlap = int(param_dict['chunk_overlap'] * param_dict['chunk_size']) ,
                separators=["\n\n", "\n", ".", " ", ""] # cut at paragraph, titles, sentences (avoids words cut)
            )

        chunks = text_splitter.create_documents([full_text]) # divides the documents (1 for now) in chunks of 'chunk_size' charachters and overlaps of 'chunk_overlap'
        # chunks is a list of pieces of text. to thee them singularly with relative metadata (not present for now), run chunks[n], where n is the n-th piece
        # takes the chunks and translate them into vectors

        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            collection_name=f"rag_trial_{uuid.uuid4().hex}"
            #persist_directory=f"{base_path}/vector_db" # for now no directory to avoid duplicates
        )
        bay_scores = []

        # train
        text_generator = pipeline(
            "text-generation",
            model = base_model,   
            tokenizer = tokenizer,
            max_new_tokens = param_dict['max_tokens'],
            repetition_penalty = param_dict['penalty'],
            temperature = param_dict['temperature'],
            do_sample = True,
            return_full_text = False,
            #device=0,  # 0: GPU, -1: CPU
            max_length = None
        )

        llm = HuggingFacePipeline(pipeline = text_generator)
        k = param_dict['top_k']
        rag_chain = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type = "stuff",
            retriever = vector_db.as_retriever(search_kwargs = {"k": k}),
            chain_type_kwargs = {"prompt": QA_CHAIN_PROMPT}
        )

        if phase == 'training':
            scores, lcb_score = training_phase(rag_chain, training_set, embedding_model)
            return scores, lcb_score

        elif phase == 'calibration':
            q_hat = calibration_phase(vector_db, rag_chain, calibration_set, embedding_model, k)
            return q_hat

        elif phase == 'test':
            ncs_scores = test_phase(vector_db, rag_chain, test_set, embedding_model, q_hat, k)
            return ncs_scores


def BO_pipeline(bay_conf, study, param_list_dict, fixing_param_dict, QA_CHAIN_PROMPT, calibration_set, full_text, embedding_model, base_model, tokenizer):
    
    bay_scores = []
    for _ in range(bay_conf):
        trial = study.ask()

        param_dict = {}
        for name, param_list in param_list_dict.items():
            if name in fixing_param_dict.keys():
                param_dict[name] = fixing_param_dict[name]
            else:
                trial.suggest_categorical(name, param_list)
                param_dict[name] = trial.params[name]

        print(param_dict)

        scores, lcb_score = run_trial(param_dict, full_text, embedding_model, QA_CHAIN_PROMPT, training_set, base_model, tokenizer, phase = 'training')
        
        # pass score to optuna
        study.tell(trial, lcb_score)
        bay_scores.append(scores)

    return study, scores



def training_phase(rag_chain, training_set, embedding_model, z_value = 1.96):

        scores = []
        for item in training_set:
            question, expected = item["question"], item["expected"]

            llm_answer = rag_chain.invoke(question)["result"]

            sim_score = semantic_similarity(expected, llm_answer, embedding_model)

            scores.append(sim_score)

            print(f"similarity_score: {sim_score:.3f}\n")

        mean_score = np.mean(scores)
        print(f"=====================================")
        print(f"mean_score: {mean_score:.3f} / 1.0")
        print(f"=====================================")
        std_score = np.std(scores, ddof=1) # ddof=1 per la deviazione standard campionaria (Bessel's correction)
        n = len(scores)
        print('scores', scores)

    # 2. Compute lower confidence bound (lcb). for now alpha = 0.05

        lcb_score = mean_score - (z_value * (std_score / np.sqrt(n)))

        print(f"=====================================")
        print(f"Trial Ended -> Mean: {mean_score:.3f} | Std: {std_score:.3f}")
        print(f"LCB score (maximize): {lcb_score:.3f}")
        print(f"=====================================")

        return scores, lcb_score


def calibration_phase(vector_db, rag_chain, calibration_set, embedding_model, k):
      print("--- Phase 4: Calibration ---\n")

      alpha = 0.1 # error tollerance
      ncs_scores = []

      for item in calibration_set:
          question, expected = item["question"], item["expected"]

          results_db = vector_db.similarity_search_with_score(question, k= k) # Non-Conformity Score)
          mean_distance = np.mean([score for doc, score in results_db])

          llm_answer = rag_chain.invoke(question)["result"] # LLM answer

          sim_score = semantic_similarity(expected, llm_answer, embedding_model) # siilarity score

          if sim_score >= 0.50: # good enough answer (### value might be tuned)
              ncs_scores.append(mean_distance)
              result = "Success"
          else:
              result = "Error"

          print(f"Question: {question[:30]}... | Distance: {mean_distance:.4f} | Sim: {sim_score:.3f} -> {result}")

      n = len(ncs_scores)
      if n == 0:
          print("\Error: No calibration possible. Zero good enough answers")

          return None
      else:
            # conformal value
            conformal_value = min(n - 1, math.ceil((n + 1) * (1 - alpha)) - 1)

            ncs_scores.sort()
            q_hat = ncs_scores[conformal_value]

            print("\n=======================================================")
            print(f"Calubration data: {n} correct answers over {len(calibration_set)}.")
            print(f"Calibrated bound (q_hat) alpha = {100 * (1 - alpha)}%: {q_hat:.4f}")
            print("=======================================================")
            return q_hat




def test_phase(vector_db, rag_chain, test_set, embedding_model, q_hat, k):
      print("--- phase 5: test ---\n")

      alpha = 0.1 # 10 % error tollerance

      ncs_scores = []
      for item in test_set:
          question, expected = item["question"], item["expected"]

          results_db = vector_db.similarity_search_with_score(question, k=k)
          mean_distance = np.mean([score for doc, score in results_db])

          llm_answer = check_answer_conformity(question, vector_db, rag_chain, q_hat, k)

          sim_score = semantic_similarity(expected, llm_answer, embedding_model)

          if sim_score >= 0.50:
                ncs_scores.append(mean_distance)
                result = "Success"
          else:
                result = "Error"
          
          print(f"Question: {question[:30]}... | Distance: {mean_distance:.4f} | Sim: {sim_score:.3f} -> {result}")

      return ncs_scores

def check_answer_conformity(question, vector_db, rag_chain, q_hat, k):
  
    results_db = vector_db.similarity_search_with_score(question, k=k)
    mean_distance = np.mean([score for doc, score in results_db])

    if mean_distance > q_hat:
        print("Rejection: No suficient information to answer to this question.")
        llm_answer = "I don't have enough information to answer to this question"
    else:
        llm_answer = rag_chain.invoke(question)["result"]
    return llm_answer