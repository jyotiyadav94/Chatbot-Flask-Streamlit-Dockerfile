import requests
import streamlit as st

# Set up Streamlit
st.title('Query the Model')
st.write('Enter your query below:')

query = st.text_input('Query:')

if st.button('Submit'):
    if query:
        response = requests.post('http://localhost:8080/query', json={'query': query})
        if response.status_code == 200:
            try:
                result = response.json().get('response')
                st.write('Response:', result)
            except requests.exceptions.JSONDecodeError:
                st.write('Error: The server did not return valid JSON.')
                st.write('Response Content:', response.text)
        else:
            st.write('Error:', response.status_code, response.text)
    else:
        st.write('Please enter a query.')