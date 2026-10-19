training_set = [
    {
        "question": "When was OmniaTech Solutions S.p.A. founded?",
        "expected": "OmniaTech Solutions S.p.A. was founded on April 14, 2008[cite: 4]."
    }

    ,
    {
        "question": "Who are the founding partners of OmniaTech Solutions S.p.A.?",
        "expected": "The founding partners are Eng. Marco Rossi and Dr. Laura Bianchi[cite: 4]."
    },
    {
        "question": "In what year did the company open its first foreign branch, and where is it located?",
        "expected": "The company opened its first foreign branch in 2021 in Berlin, Germany[cite: 4]."
    },
    {
        "question": "What is the company's target regarding environmental sustainability?",
        "expected": "The company's target is zero emissions by 2030[cite: 4]."
    },
    {
        "question": "What was the initial focus of the company when it was established?",
        "expected": "It was initially established as a start-up for the development of management software for the manufacturing sector[cite: 4]."
    },
    {
        "question": "What is the permitted entry window for employees?",
        "expected": "The permitted entry window is from 08:00 to 10:00[cite: 4]."
    },
    {
        "question": "Between what hours can the lunch break be taken?",
        "expected": "The lunch break can be taken between 12:30 and 14:30[cite: 4]."
    },
    {
        "question": "What is the maximum duration allowed for a lunch break?",
        "expected": "The maximum duration of the break is 90 minutes[cite: 4]."
    },
    {
        "question": "How much notice must a Line Manager give to formally request overtime?",
        "expected": "Overtime must be formally requested with at least 48 hours' notice[cite: 4]."
    },
    {
        "question": "What is the annual maximum limit for allowed overtime hours?",
        "expected": "The maximum limit is no more than 250 hours per year[cite: 4]."
    },
    {
        "question": "What is the overtime surcharge for hours worked on a Sunday?",
        "expected": "Overtime hours worked on Sundays are subject to a 50% surcharge[cite: 4]."
    },
    {
        "question": "What is the value of the meal voucher for a day of Smart Working?",
        "expected": "In the case of Smart Working, the value of the meal voucher is 5.00 Euros[cite: 4]."
    },
    {
        "question": "By what day of the month are meal vouchers loaded onto the LunchCard?",
        "expected": "Meal vouchers are loaded onto the LunchCard by the 10th day of the following month[cite: 4]."
    },
    {
        "question": "How many working days of holiday does a full-time employee accrue per year?",
        "expected": "Each full-time employee accrues 26 working days of holiday per year[cite: 4]."
    },
    {
        "question": "During which period must employees take at least two consecutive weeks of holiday?",
        "expected": "Holidays must be taken for at least two consecutive weeks during the period between June 1 and September 30[cite: 4]."
    },
    {
        "question": "How much notice is required for holiday requests exceeding 3 consecutive days?",
        "expected": "Holiday requests exceeding 3 consecutive days require at least 30 days' notice[cite: 4]."
    },
    {
        "question": "What happens to unused holiday balances at the end of the year following their accrual?",
        "expected": "Unused holiday balances cannot be monetized, but must mandatorily be taken[cite: 4]."
    },
    {
        "question": "Within what timeframe must an employee communicate the INPS medical certificate protocol number in case of sick leave?",
        "expected": "The protocol number must be communicated to the company within 48 hours from the start of the absence[cite: 4]."
    },
    {
        "question": "What consequence does an employee face if they fail to communicate the INPS protocol number on time?",
        "expected": "Failure to provide this communication will result in the absence being considered unjustified[cite: 4]."
    },
    {
        "question": "How many additional days of paid parental leave does the company grant within the first year of a child's life?",
        "expected": "The company grants 15 additional working days of paid leave[cite: 4]."
    },
    {
        "question": "How long is the probationary period an employee must pass before joining the Smart Working program?",
        "expected": "Employees must pass a 6-month probationary period[cite: 4]."
    },
    {
        "question": "What is the maximum number of allowed remote working days per month?",
        "expected": "The maximum number of allowed remote working days is 12 days per month[cite: 4]."
    },
    {
        "question": "Can unused Smart Working days be carried over to the next month?",
        "expected": "No, they are not cumulative and are reset to zero if not used in the reference calendar month[cite: 4]."
    },
    {
        "question": "How much is the domestic utilities reimbursement for an employee using 10 days of agile work in a month?",
        "expected": "The reimbursement is a flat-rate net allowance of 25.00 Euros per month[cite: 4]."
    },
    {
        "question": "Is it allowed to process unencrypted sensitive data while working in a public bar?",
        "expected": "No, it is forbidden to work in unsafe public places if the activities involve processing unencrypted sensitive data[cite: 4]."
    },
    {
        "question": "What is the capital city of Australia?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "How do you bake a traditional chocolate cake?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "Who won the FIFA World Cup in 2018?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What is the average distance between the Earth and the Moon?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "Can you explain how photosynthesis works in plants?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What are the main ingredients needed to make a Margherita pizza?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "Who is the author of the dystopian novel '1984'?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What is the exact chemical formula for table salt?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "How many planets are officially recognized in our Solar System?",
        "expected": "I don't have enough information to answer to this question"
    }

]


calibration_set = [
    {
        "question": "What is the minimum distance from the hiring location for a trip to be considered a business trip?",
        "expected": "The distance from the hiring location must exceed 50 km[cite: 4]."
    },
    {
        "question": "What application must be used to authorize business trips before departure?",
        "expected": "All business trips must be authorized via the TravelFlow application[cite: 4]."
    },
    {
        "question": "What is the maximum reimbursable limit for dinner during a trip in Italy?",
        "expected": "The maximum reimbursable limit for dinner in Italy is 40.00 Euros[cite: 4]."
    },
    {
        "question": "What is the daily total food expense limit for trips in Europe?",
        "expected": "The daily total food expense limit for trips in Europe is 90.00 Euros[cite: 4]."
    },
    {
        "question": "Do employees need to submit receipts for meals during Extra-EU trips?",
        "expected": "No, they receive a flat-rate daily total (Per Diem) of 120.00 Euros without the need to submit receipts[cite: 4]."
    },
    {
        "question": "Are alcoholic beverages reimbursable during business trips?",
        "expected": "Alcoholic beverages are not reimbursable, with the exception of one glass of wine or beer during evening meals[cite: 4]."
    },
    {
        "question": "What is the maximum accommodation expense limit per night abroad?",
        "expected": "For abroad, the accommodation limit is raised to 200.00 Euros[cite: 4]."
    },
    {
        "question": "Can an employee claim reimbursement for pay-TV services in a hotel?",
        "expected": "No, expenses for pay-TV services in hotels are not reimbursable[cite: 4]."
    },
    {
        "question": "What is the mileage reimbursement rate for a 100% electric vehicle?",
        "expected": "The fixed mileage reimbursement rate for 100% electric vehicles is 0.55 Euros/km[cite: 4]."
    },
    {
        "question": "Are highway tolls included in the fixed mileage reimbursement rate?",
        "expected": "No, highway tolls will be reimbursed separately upon presentation of a receipt[cite: 4]."
    },
    {
        "question": "What is the minimum required length for a company password?",
        "expected": "Passwords must have a minimum length of 14 characters[cite: 4]."
    },
    {
        "question": "How often must passwords be changed?",
        "expected": "It is mandatory to change the password every 60 days[cite: 4]."
    },
    {
        "question": "Can an employee reuse any of their previously used passwords?",
        "expected": "It is not possible to reuse any of the last 5 previously used passwords[cite: 4]."
    },
    {
        "question": "What type of mass storage devices are allowed to be connected to company computers?",
        "expected": "The only allowed peripherals are those provided and encrypted by the company's IT department[cite: 4]."
    },
    {
        "question": "What keyboard shortcut is mentioned to lock a Windows computer screen?",
        "expected": "The shortcut is Windows Key + L[cite: 4]."
    },
    {
        "question": "What is the highest mountain peak in the world?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What are the basic rules for moving a knight in chess?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What is the current population of the metropolitan area of Tokyo?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "Who directed the sci-fi movie 'Inception'?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "How many points is a free throw worth in basketball?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What is the correct way to say 'thank you' in Japanese?",
        "expected": "I don't have enough information to answer to this question"
    }

]

test_set = [
    {
        "question": "Where must sensitive paper documents be stored at the end of the working day?",
        "expected": "They must be stored in the appropriate locked cabinets[cite: 4]."
    },
    {
        "question": "During which dates does the annual performance evaluation take place?",
        "expected": "The performance evaluation takes place annually between January 15 and February 15[cite: 4]."
    },
    {
        "question": "What is the maximum potential MBO bonus as a percentage of the Gross Annual Salary?",
        "expected": "The maximum potential bonus is equal to 15% of the Gross Annual Salary (RAL)[cite: 4]."
    },
    {
        "question": "In which month's payslip is the MBO bonus paid?",
        "expected": "The bonus is paid with the March payslip of the following year[cite: 4]."
    },
    {
        "question": "What disciplinary sanction applies for an unjustified delay of less than 15 minutes twice in a month?",
        "expected": "A verbal warning applies for minor infractions such as an unjustified delay of less than 15 minutes twice in a month[cite: 4]."
    },
    {
        "question": "What is the maximum deduction from a payslip for a disciplinary fine?",
        "expected": "The deduction is up to a maximum of 4 hours of normal pay[cite: 4]."
    },
    {
        "question": "For what kind of infraction can a suspension of up to 10 days be applied?",
        "expected": "It is applied for serious violations of the ethical code or insubordination towards a superior[cite: 4]."
    },
    {
        "question": "How many working days does an employee have to present justifications after receiving a disciplinary dispute?",
        "expected": "The employee has 5 working days from receipt to present their justifications[cite: 4]."
    },
    {
        "question": "Through which portal must voluntary resignations be submitted?",
        "expected": "Resignations must be submitted exclusively electronically via the Ministry of Labour portal[cite: 4]."
    },
    {
        "question": "By what time must an outgoing employee return all company equipment on their last working day?",
        "expected": "Company equipment must be returned no later than 12:00 PM on their last actual working day[cite: 4]."
    },
    {
        "question": "What is the speed of light in a vacuum?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "Which artist painted the Mona Lisa?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What tectonic processes are responsible for causing earthquakes?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "How many bones are there in an adult human body?",
        "expected": "I don't have enough information to answer to this question"
    },
    {
        "question": "What is the official currency used in the United Kingdom?",
        "expected": "I don't have enough information to answer to this question"
    }

]