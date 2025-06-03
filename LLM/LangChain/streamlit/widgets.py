import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="🧩 Streamlit Widgets",
    page_icon="🎛️",
    layout="centered"
)

st.title("🎛️ Interactive Widgets Demo")

# Text input
name = st.text_input("Enter your name")
if name:
    st.write(f"👋 Hello, {name}!")

st.divider()

# Number input
x = st.number_input("Enter a number", min_value=1, max_value=99, step=1)
st.write(f"📌 Current number is: {x}")

st.divider()

# Button
clicked = st.button("Click me")
if clicked:
    st.write("👻👻👻 You clicked the button!")
