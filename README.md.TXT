# Uncertainty-Aware RAG: Bayesian Optimization & Conformal Prediction (Work in Progress)

An end-to-end **Retrieval-Augmented Generation (RAG)** pipeline with hyperparameter tuning. 

This project introduces:
1. **Iterative Bayesian Optimization (Optuna):** Optimizing retrieval and generation hyperparameters by maximizing the **Lower Confidence Bound (LCB)** of semantic similarity.

2. **Split Conformal Prediction:** Calibrating an empirical quantile threshold ($\hat{q}$) to statistically guarantee an error/rejection rate bounded by $\alpha$, limitating out-of-context answers.

## Project Structure
* `data/`: Synthetic corporate policy dataset (`omniatech.txt`) and prompt templates.
* `notebooks/`: Complete pipeline, Training (BO), Calibration (Conformal Prediction), and Testing phases.

## Setup
```bash
pip install -r requirements.txt