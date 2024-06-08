
import streamlit as st
import pandas as pd
import pickle

st.title("Customer Churn Prediction")

gender = st.radio('Gender', ['Male', 'Female'])
SeniorCitizen = st.radio('Senior Citizen', ['No', 'Yes'])
Partner = st.radio('Partner', ['No', 'Yes'])
Dependents = st.radio('Dependents', ['No', 'Yes'])
tenure = st.number_input("Tenure", min_value=1)
PhoneService = st.radio('Phone Service', ['No', 'Yes'])
MultipleLines = st.radio('Multiple Lines', ['No phone service', 'No', 'Yes'])
InternetService = st.radio('Internet Service', ['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.radio('Online Security', ['No', 'Yes', 'No internet service'])
OnlineBackup = st.radio('Online Backup', ['Yes', 'No', 'No internet service'])
DeviceProtection = st.radio('Device Protection', ['Yes', 'No', 'No internet service'])
TechSupport = st.radio('Tech Support', ['Yes', 'No', 'No internet service'])
StreamingTV = st.radio('Streaming TV', ['Yes', 'No', 'No internet service'])
StreamingMovies = st.radio('Streaming Movies', ['Yes', 'No', 'No internet service'])
Contract = st.radio('Contract', ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.radio('Paperless Billing', ['Yes', 'No'])
PaymentMethod = st.radio('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
MonthlyCharges = st.number_input("Monthly Charges", min_value=5, max_value=100)
TotalCharges = st.number_input("Total Charges", min_value=10, max_value=1000)

if st.button('Predict Churn'):
    input_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [SeniorCitizen],
        'Partner': [Partner],
        'Dependents': [Dependents],
        'tenure': [tenure],
        'PhoneService': [PhoneService],
        'MultipleLines': [MultipleLines],
        'InternetService': [InternetService],
        'OnlineSecurity': [OnlineSecurity],
        'OnlineBackup': [OnlineBackup],
        'DeviceProtection': [DeviceProtection],
        'TechSupport': [TechSupport],
        'StreamingTV': [StreamingTV],
        'StreamingMovies': [StreamingMovies],
        'Contract': [Contract],
        'PaperlessBilling': [PaperlessBilling],
        'PaymentMethod': [PaymentMethod],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges]
    })
    
    with open(r"C:\Users\user\Desktop\churn_prediction\random_forest_model.pkl", 'rb') as file:
        pipeline = pickle.load(file)

    prediction = pipeline.predict(input_data)
    
    if prediction[0] == 1:
        st.write("The customer is likely to churn.")
    else:
        st.write("The customer is not likely to churn.")