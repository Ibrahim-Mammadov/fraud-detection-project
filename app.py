# app.py
import streamlit as st
import joblib

st.title("Fraud Detection System") # Buranı onsuz da belə yazmışdıq
amount = st.number_input("Transaction Amount:") # "Tranzaksiya məbləği" -> "Transaction Amount"
time = st.number_input("Transaction Hour:") # "Tranzaksiya saatı" -> "Transaction Hour"

if st.button("Check"): # "Yoxla" -> "Check"
    model = joblib.load('model.pkl')
    prediction = model.predict([[amount, time]])
    
    if prediction[0] == 1:
        st.error("Warning: Fraud detected!") # Mesajı da ingiliscə etdik
    else:
        st.success("Safe transaction.") # Mesajı da ingiliscə etdik