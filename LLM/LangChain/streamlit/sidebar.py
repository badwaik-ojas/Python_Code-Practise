import streamlit as st

# Title
st.title("🌍 Layout with Sidebar")

# Sidebar Select Box
my_selectbox = st.sidebar.selectbox(
    "Choose a country",
    ["US", "UK", "DE", "FR"]
)

# Sidebar Slider
my_slider = st.sidebar.slider(
    "Select temperature (°C)",
    min_value=-20,
    max_value=50,
    value=22
)

# Main Area Display
st.write(f"📌 You selected **{my_selectbox}**")
st.write(f"🌡️ Temperature is set to **{my_slider}°C**")
