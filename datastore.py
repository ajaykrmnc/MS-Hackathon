import streamlit as st
def table(collection):
    # Query the collection and sort the data in ascending order based on the level of disease
    st.title("Admin Dashboard")
    st.subheader("Emergency Queue for each disease")
    # Create a dictionary to store the rows for each disease type
    disease_rows = {}
    sorted_data = collection.find().sort('level_of_disease', 1)
    # Iterate over each document in the sorted_data
    for document in sorted_data:
        # Extract the relevant fields from the document
        name = document['user_name']
        disease = document['kind_of_disease']
        level = document['level_of_disease']
        
        # Create a row with the extracted data
        row = [name, disease, level]
        # Check if the disease type already exists in the dictionary
        if disease in disease_rows:
            # If it exists, append the row to the existing list of rows for that disease type
            disease_rows[disease].append(row)
        else:
            # If it doesn't exist, create a new list with the row and add it to the dictionary
            disease_rows[disease] = [row]
    
    # Display the data in separate tables for each disease type
    for disease, rows in disease_rows.items():
        st.write(f"Table for {disease} disease:")
        st.table(rows)