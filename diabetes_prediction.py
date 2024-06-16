import streamlit as st

def diabetes_prediction(diabetes_model, collection):
    st.title('Diabetes Prediction using ML')
    st.write("Enter your test report")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input('Enter your Name', placeholder='Jane Doe')

    with col2:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder='2')

    with col3:
        Glucose = st.text_input('Glucose Level', placeholder='130')

    with col1:
        BloodPressure = st.text_input('Blood Pressure value', placeholder='85')

    with col2:
        SkinThickness = st.text_input('Skin Thickness value', placeholder='32')

    with col3:
        Insulin = st.text_input('Insulin Level', placeholder='120')

    with col1:
        BMI = st.text_input('BMI value', placeholder='28.5')

    with col2:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder='0.627')

    with col3:
        Age = st.text_input('Age of the Person', placeholder='45')

    diab_diagnosis = ''
    prediction = 0

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])
        prediction = diab_prediction[0]

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    if diab_diagnosis != '':
        st.success(diab_diagnosis)
    emergency_input = {
        'user_name': name,
        'kind_of_disease': 'Diabetes',
        'level_of_disease': prediction
    }

    if st.button('Enter into Emergency Queue'):
        if name != '':
            collection.insert_one(emergency_input)

