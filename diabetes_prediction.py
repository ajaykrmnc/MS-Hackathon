import streamlit as st

def diabetes_prediction(diabetes_model, collection):
    st.title('Diabetes Prediction using ML')
    st.write("Enter your test report")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input('Enter you Name')
    with col2:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col3:
        Glucose = st.text_input('Glucose Level')
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
    with col3:
        Insulin = st.text_input('Insulin Level')
    with col1:
        BMI = st.text_input('BMI value')
    with col2:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col3:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    diab_prediction = 0

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    if st.button('Enter into Emergency Queue'):
        emergency_input = [name, 'Diabetes', diab_prediction]
        collection.save_one(emergency_input);
    if diab_diagnosis != '':
        st.success(diab_diagnosis)

