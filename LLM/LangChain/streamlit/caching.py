import streamlit as st
import time

@st.cache_data
def slow_addition(a, b):
    time.sleep(2)  # simulate long operation
    return a + b

x = st.number_input("Enter x:", value=5)
y = st.number_input("Enter y:", value=3)
result = slow_addition(x, y)
st.write("Result (cached):", result)
