import streamlit as st

st.title("This is a Price Calculator")

product_price=st.number_input("Product Price",placeholder="Enter your product price here...")

st.subheader("Select the discount from 0 to 50%")
discount=st.slider("Discount Percentage",0,50,0)

d_price=product_price-(product_price*discount/100)
if st.button("Submit"):
    st.write(f"The price of the product after getting a discount of {discount} is: {d_price} ")

header=['Before','After']
price=[product_price,d_price]
tables=[header,price]
st.table(tables)