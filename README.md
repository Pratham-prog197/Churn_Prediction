# 📉 Customer Churn Prediction System
## 📌 Project Overview
Customer churn is one of the biggest challenges faced by telecom companies because losing existing customers directly impacts revenue and growth.  

This project uses Machine Learning to predict whether a customer is likely to leave the company based on factors such as:
- contract type
- monthly charges
- tenure
- payment method
- internet service
- customer demographics

The project follows a complete end-to-end Machine Learning workflow including:
- data preprocessing
- exploratory data analysis
- handling imbalanced data
- model training
- evaluation
- deployment using Streamlit & Hugging Face Spaces

## 🎯 Why I Chose This Project

I chose this project because customer retention is a real-world business problem that directly affects company profitability.  

Instead of only creating dashboards, I wanted to build a Machine Learning system capable of:
- predicting customer churn
- identifying high-risk customers
- generating business insights
- supporting retention strategies

This project also helped me strengthen my understanding of:
- classification algorithms
- data preprocessing
- feature engineering
- model evaluation
- deployment of ML applications
## 🧠 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Machine Learning
- Classification Algorithms
- Feature Engineering
- Model Evaluation
- Deployment using Streamlit
- Business Problem Solving

# 🚨 Problem Statement

Telecom companies lose customers frequently due to:
- high monthly charges
- short-term contracts
- poor service satisfaction
- competitive alternatives

Manually identifying customers likely to churn is difficult and inefficient.

The objective of this project is to:
✅ Predict customer churn accurately  
✅ Identify important churn-driving factors  
✅ Help businesses improve customer retention  

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit
- Hugging Face Spaces

- ### 📂 Dataset Information

The project uses the Telco Customer Churn dataset containing customer information such as:
- gender
- tenure
- monthly charges
- contract type
- payment method
- internet service
- churn status

- # ⚙️ Machine Learning Workflow

## 1️⃣ Data Cleaning
- removed unnecessary columns
- handled missing values
- corrected data types

## 2️⃣ Exploratory Data Analysis
Performed EDA to identify customer churn patterns and behavior trends.

## 3️⃣ Feature Encoding
Converted categorical features into numerical format using Label Encoding.

## 4️⃣ Handling Imbalanced Data
Used SMOTE to balance churn and non-churn classes.

## 5️⃣ Model Training
Trained and compared multiple ML classification models:
- Decision Tree
- Random Forest
- Gradient Boosting

## 6️⃣ Model Evaluation
Evaluated performance using:
- Accuracy Score
- Confusion Matrix
- ROC Curve

## 7️⃣ Deployment
Deployed the trained model using Streamlit on Hugging Face Spaces.

# 🤖 Best Performing Model

Among all tested models, the tuned XGBoost model performed best with a recall of 92% and ROC-AUC of 0.86. 
Since customer churn prediction is a high-recall business problem, I
optimized the prediction threshold to 0.35 to proactively identify most at-risk customers

# 📊 Key Business Insights

### 🔹 Customers with month-to-month contracts showed the highest churn behavior.

### 🔹 Customers with higher monthly charges were more likely to leave the service.

### 🔹 Short-tenure customers had significantly higher churn probability.

### 🔹 Customers using electronic check payment methods showed increased churn rates.

### 🔹 Long-term contract customers were more loyal and stable.
