import streamlit as st

def parkinsons_prediction(parkinsons_model, collection):
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP Fo(Hz)', placeholder='119.992')
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)', placeholder='157.302')
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)', placeholder='74.997')
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)', placeholder='0.00784')
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)', placeholder='0.00007')
    with col1:
        RAP = st.text_input('MDVP: RAP', placeholder='0.00370')
    with col2:
        PPQ = st.text_input('MDVP: PPQ', placeholder='0.00554')
    with col3:
        DDP = st.text_input('Jitter: DDP', placeholder='0.01109')
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer', placeholder='0.04374')
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)', placeholder='0.426')
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3', placeholder='0.02182')
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5', placeholder='0.03130')
    with col3:
        APQ = st.text_input('MDVP: APQ', placeholder='0.02971')
    with col4:
        DDA = st.text_input('Shimmer: DDA', placeholder='0.06534')
    with col5:
        NHR = st.text_input('NHR', placeholder='0.02211')
    with col1:
        HNR = st.text_input('HNR', placeholder='21.033')
    with col2:
        RPDE = st.text_input('RPDE', placeholder='0.414783')
    with col3:
        DFA = st.text_input('DFA', placeholder='0.815285')
    with col4:
        spread1 = st.text_input('spread1', placeholder='-4.813031')
    with col5:
        spread2 = st.text_input('spread2', placeholder='0.266482')
    with col1:
        D2 = st.text_input('D2', placeholder='2.301442')
    with col2:
        PPE = st.text_input('PPE', placeholder='0.284654')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    if parkinsons_diagnosis != "":
        st.success(parkinsons_diagnosis)
