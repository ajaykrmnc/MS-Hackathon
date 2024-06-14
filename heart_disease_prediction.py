import streamlit as st

def heart_disease_prediction(heart_disease_model, collection):
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input('Enter your name')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        age  = st.text_input('Age', value=45)
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', value=140)
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', value=240)
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', value=1)
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', value=1)
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', value=150)
    with col3:
        exang = st.text_input('Exercise Induced Angina', value=1)
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', value=1)
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', value=2)
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', value=1)
    with col1:
        cp = st.text_input('Chest Pain types', value=2)
    with col2:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value=1)

    heart_diagnosis = ''
    heart_prediction = ''

    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    if st.button('Enter into Emergency Queue'):
        emergency_input = [name, 'Heart Disease', heart_prediction]
        collection.save_one(emergency_input)
    if heart_diagnosis != '':
        st.success(heart_diagnosis)
