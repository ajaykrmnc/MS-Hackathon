import streamlit as st
import pandas as pd
import plotly.express as px


def create_pie_chart(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Count the number of occurrences of each disease
    disease_counts = df['kind_of_disease'].value_counts().reset_index()
    disease_counts.columns = ['Disease', 'Count']
    
    # Create a pie chart
    fig = px.pie(disease_counts, names='Disease', values='Count', title='Number of People with Each Disease')
    return fig

def display_tables(data):
    st.subheader("Emergency Queue for Each Disease")
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Sort the data by disease and level of disease
    df_sorted = df.sort_values(by=['kind_of_disease', 'level_of_disease'])
    
    # Display tables for each disease
    for disease in df['kind_of_disease'].unique():
        st.write(f"Table for {disease} Disease:")
        disease_data = df_sorted[df_sorted['kind_of_disease'] == disease]
        st.table(disease_data[['user_name', 'kind_of_disease', 'level_of_disease']])


def table(collection):
    # Fetch data from MongoDB collection
    data = list(collection.find())
    # Create and display pie chart

    # Main Streamlit app
    st.title("Admin Dashboard")
    col1, col2 = st.columns([3, 2])
    with col1:
        display_tables(data)
    with col2:
        st.subheader("Disease Distribution")
        pie_chart = create_pie_chart(data)
        st.plotly_chart(pie_chart)


# Display tables for each disease
