import streamlit as st
import mysql.connector
import numpy as np
import joblib

model = joblib.load("Logistic.pkl")

# mysql connection

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change this
        password="Saipranith@2003",  # Change this
        database="heart_data"   
    )
    
    
# Streamlit app
st.title("Heart Disease Prediction")

age = st.number_input('Age', min_value=1, max_value=120)
sex = st.selectbox('sex (0: Male, 1: Female)', [0, 1])
bp = st.number_input('Blood Pressure (bp)', min_value = 80, max_value = 200)
cholesterol = st.number_input('Cholesterol (mg/dL)', min_value=100, max_value=600)

if st.button('Predict'):
    user_data = np.array([[age, sex, bp, cholesterol]])
    prediction = model.predict(user_data)[0]
    
    st.write(f"Prediction: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}")
    
    #store user in database
    
    db = connect_to_db()
    cursor = db.cursor()
    
    query = """"""
    INSERT INTO user_inputs (age, sex, bp, cholesterol, heart_disease)
    VALUES (%s, %s, %s, %s, %s)
    