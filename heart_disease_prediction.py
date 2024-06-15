import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import pickle
import numpy as np

def heart_disease_prediction(heart_disease_model, collection):
    
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input('Name')

    with col2:
        sex = st.text_input('Sex M: 0, F: 1')

    with col3:
        age = st.text_input('Age')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    with col2:
        cp = st.text_input('Chest Pain types')

    # code for Prediction
    heart_diagnosis = ''
    prediction = 0

    # creating a button for Prediction
    scaler_heart = pickle.load(open('./saved_models/scaler_heart.pkl', 'rb'))
    
    if st.button('Heart Disease Test Result'):

        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
       
        input_data = [float(x) for x in input_data]
        
        input_data=scaler_heart.transform([input_data])
        #print(input_data)
        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)
        #print(input_data)
        #reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        
        prediction = heart_disease_model.predict(input_data)
        #print(prediction)
        
        if prediction[0]== 1:
            heart_diagnosis = "The person has Heart Disease"
        else:
            heart_diagnosis = "The person does not have Heart Disease"

        st.success(heart_diagnosis)
    
    if heart_diagnosis != '':
        st.success(heart_diagnosis)
        if st.button('Enter into Emergency Queue'):
            emergency_input = {
            'user_name': name,
            'kind_of_disease': 'Heart',
            'level_of_disease': prediction
        }
        collection.insert_one(emergency_input)
