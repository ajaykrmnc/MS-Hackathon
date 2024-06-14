import streamlit as st

def parkinsons_prediction(parkinsons_model):
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP: RAP')
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
    with col3:
        DDP = st.text_input('Jitter: DDP')
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
    with col3:
        APQ = st.text_input('MDVP: APQ')
    with col4:
        DDA = st.text_input('Shimmer: DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

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
