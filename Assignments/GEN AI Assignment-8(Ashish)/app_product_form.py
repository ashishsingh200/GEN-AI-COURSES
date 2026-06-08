import streamlit as st

st.title("This is a Product form....")
st.sidebar.header("Product Form")

prod_name=st.sidebar.text_input("Product Name",placeholder="Enter the name of the products....")

prod_category=st.sidebar.selectbox(
    "Category",
    ['Stationary','dairy','electrical','textiles']
)

price=st.sidebar.number_input("Price",value=0)

if st.sidebar.button("Add Product"):
    st.write("Products Added Successfully!")

    st.subheader("Details of the product added...")
    st.write(f"Product Name: {prod_name}")
    st.write(f"Category: {prod_category} ")
    st.write(f"Price: {price}")
    