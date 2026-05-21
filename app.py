import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ----------------------------
# Load Saved Model & Encoders
# ----------------------------

model = pickle.load(open("churn_model.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# ----------------------------
# Title Section
# ----------------------------

st.title("📉 Customer Churn Prediction System")
st.markdown("Predict whether a telecom customer is likely to churn.")

st.divider()

# ----------------------------
# Input Section
# ----------------------------

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

with col2:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

# ----------------------------
# Prediction Button
# ----------------------------

if st.button("🔍 Predict Churn"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior_citizen],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    # ----------------------------
    # Apply Label Encoding
    # ----------------------------

    for column in input_data.columns:

        if column in label_encoders:

            input_data[column] = label_encoders[column].transform(
                input_data[column]
            )

    # ----------------------------
    # Prediction
    # ----------------------------

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    # ----------------------------
    # Output Section
    # ----------------------------

    if prediction == 1:

        st.error("⚠️ Customer is likely to CHURN")

    else:

        st.success("✅ Customer is NOT likely to churn")

    st.subheader(f"Churn Probability: {probability:.2%}")

    # ----------------------------
    # Risk Level
    # ----------------------------

    if probability < 0.30:

        st.success("🟢 Low Risk Customer")

    elif probability < 0.70:

        st.warning("🟠 Medium Risk Customer")

    else:

        st.error("🔴 High Risk Customer")

# ----------------------------
# Footer
# ----------------------------

st.divider()

st.markdown(
    "Built with ❤️ using Streamlit & Machine Learning"
)