import streamlit as st

st.title("Welcome to Streamlit!")

input=st.text_input("Name",placeholder="Enter Your name here...")

if st.button("Greet Me"):
    st.write(f"Hello, {input} !")