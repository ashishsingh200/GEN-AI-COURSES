import streamlit as st

st.title("Simple Sales Dashboard")

selected_month=st.selectbox("Months",
             ['January','February','March','April'],
             placeholder="Select a month",
             index=None
             )

sales={
    'January':1200,
    'February':1500,
    'March': 900,
    'April':2000
}

if selected_month:
    current_sales=sales[selected_month]
    st.metric(label=f"Sales for {selected_month}", value=f"${current_sales: ,}")

st.divider()

st.subheader("Monthly sales Overview")
st.bar_chart(list(sales.values()))