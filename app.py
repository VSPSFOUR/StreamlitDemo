# app.py (for Streamlit)
import streamlit as st

# Set up Streamlit
st.title("Receive Data from Google Colab")

# Get data from URL parameters
query_params = st.experimental_get_query_params()
data = query_params.get("data", ["No data received"])[0]

# Display the received data
st.write(f"Data from Colab: {data}")
