import streamlit as st

def home():
    st.title("AI Medical Health App")
    st.write("Welcome to the AI Medical Health App! Please enter your symptoms below:")
    st.write("We provide the following services:")
    col1, col2 = st.columns(2)
    with col1:
        st.write("1. BMI Calculator")
        st.write("2. Parkinson's Disease Prediction")
        st.write("3. Diabetes Prediction")
        st.write("4. Heart Disease Prediction")
        st.write("5. Breast Cancer Prediction")
        st.write("6. Chatbot")
    with col2:
        st.image("assets/doctor.png")

    
    st.write("Please select the service you want to use from the sidebar.")
    
