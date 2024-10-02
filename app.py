# # app.py
# import streamlit as st

# # Streamlit app to display data
# st.title("Data from Google Colab")

# # Create a placeholder for incoming data
# if 'data' not in st.session_state:
#     st.session_state.data = ""

# # Display the received data
# st.write("Data from Colab:", st.session_state.data)

# # Create an input box for testing
# input_data = st.text_input("Send data from Colab:")
# if input_data:
#     st.session_state.data = input_data
# # https://appdemo-jazjcopgbm8lcjljatjivg.streamlit.app/

# app.py
import streamlit as st

st.title("Data from Google Colab")

# Get data from URL parameters
data = st.experimental_get_query_params().get("data", [""])[0]

# Display the received data
st.write("Data from Colab:", data)
