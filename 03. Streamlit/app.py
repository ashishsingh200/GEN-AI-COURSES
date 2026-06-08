import streamlit as st
import pandas as pd
st.write('Hello World')

st.title("Hello Streamlit")
st.write("Ashish Kumar Singh")

st.header("welcome to Streamlit")

st.subheader("This is a Sub-header")
st.text("THis is a plain text")

# Buttons, Checkboxex and Slicers

if st.button("Buttom"):
    st.write("Button Clicked")

agree= st.checkbox("I agree")
if agree:
    st.write("you agreed")

level = st.slider("Select a level:",1,10,3)
st.write(f"Selected level is: {level}")

uploaded_file=st.file_uploader("Upload a File",type=['csv'])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())