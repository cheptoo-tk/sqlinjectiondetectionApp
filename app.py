import streamlit as st
from transformers import pipeline


pipeline = pipeline("text-classification", model="cybersectony/sql-injection-attack-detection-distilbert")

st.title("SQL Injection Detection")

message = st.text_input('Enter a SQL Query')
submit = st.button('Predict')


if submit:
    
    result = pipeline(message)
    print(result)

    if result[0]['label'] == 'LABEL_1':
        st.warning('SQL Injection detected!')
    else:
        st.success('No SQL Injection detected!')
    
    st.balloons()

st.caption("Made with by @cybersectony. Credits to 🤗 Spaces for Hosting this ")
