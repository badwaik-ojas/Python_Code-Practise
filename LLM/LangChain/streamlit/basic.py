# demo_app.py
import streamlit as st

st.title("🌡️ Temperature Converter")
celsius = st.slider("Temperature in Celsius", -100, 100, 0)
fahrenheit = (celsius * 9/5) + 32
st.write(f"{celsius}°C is {fahrenheit}°F")
