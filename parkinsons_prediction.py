import streamlit as st

def parkinsons_prediction(parkinsons_model, collection):
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        name = st.text_input('Enter your name', value='John Doe')
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)', value=157.302)
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)', value=74.997)
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)', value=0.00784)
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)', value=0.00007)
    with col1:
        RAP = st.text_input('MDVP: RAP', value=0.00370)
    with col2:
        PPQ = st.text_input('MDVP: PPQ', value=0.00554)
    with col3:
        DDP = st.text_input('Jitter: DDP', value=0.01109)
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer', value=0.04374)
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)', value=0.426)
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3', value=0.02182)
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5', value=0.03130)
    with col3:
        APQ = st.text_input('MDVP: APQ', value=0.02971)
    with col4:
        DDA = st.text_input('Shimmer: DDA', value=0.06534)
    with col5:
        NHR = st.text_input('NHR', value=0.02211)
    with col1:
        HNR = st.text_input('HNR', value=21.033)
    with col2:
        RPDE = st.text_input('RPDE', value=0.414783)
    with col3:
        DFA = st.text_input('DFA', value=0.815285)
    with col4:
        spread1 = st.text_input('spread1', value=-4.813031)
    with col5:
        spread2 = st.text_input('spread2', value=0.266482)
    with col1:
        D2 = st.text_input('D2', value=2.301442)
    with col2:
        PPE = st.text_input('PPE', value=0.284654)
    with col3:
        fo = st.text_input('MDVP Fo(Hz)', value=119.992)

    parkinsons_diagnosis = ''
    prediction = 0

    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])
        prediction = parkinsons_prediction[0]
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    if parkinsons_diagnosis != "":
        st.success(parkinsons_diagnosis)
    emergency_input = {
            'user_name': name,
            'kind_of_disease': 'Parkinsons_preiction',
            'level_of_disease': prediction
    }
    if st.button('Enter into Emergency Queue'):
        if name != '':
            collection.insert_one(emergency_input)
