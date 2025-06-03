# temp_converter.py
import streamlit as st

st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")

st.title("🌡️ Temperature Converter")

@st.cache_data
def convert_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

c = st.slider("Temperature in Celsius", -100, 100, 25)
f = convert_to_fahrenheit(c)

st.success(f"{c}°C = {f}°F")
