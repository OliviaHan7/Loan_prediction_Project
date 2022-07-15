# Mini-project IV


## Project/Goals
The goal of this project is to build a machine learning model to predict the loan eligibility of applicants based on their Gender, Marital Staus, Education background, Credit Card History, Number of Dependents, Income, Loan Amount, and Term.  


## Hypothesis

1. Applicants having a good credit history are likely get approval.
2. Applicants with higher applicant and co-applicant incomes
3. Applicants with higher education level

## EDA 


## Process
- Data Preparation
- Feature Engineering
- Supervised Learning
- Pipelines
- Model Persistance
- Flask - building an API
- Deployment to Cloud (AWS)


## Results/Demo
I used RandomForestClassifier. 
The accuracy score is 79% using basemodel.
After gridSearch, the score goes up to 81.9%

## Future Goals
1. The dataset is highly imbalanced. I could use oversamling technique to increase the model accuracy.
2. There are more hidden relationship among the features.