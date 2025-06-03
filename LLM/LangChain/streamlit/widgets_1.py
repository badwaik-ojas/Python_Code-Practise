import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Widgets - Part 2",
    page_icon="🧩",
    layout="centered"
)

st.title("🧩 Streamlit Widgets — Part 2")

agree = st.checkbox("I agree")

if agree:
    st.write("✅ Great! You agreed.")

st.divider()

checked = st.checkbox("Continue?", value=True)

if checked:
    st.write("🟢" * 5)

st.divider()

df = pd.DataFrame({
    "Name": ["Ann", "Mario", "Douglas"],
    "Age": [30, 25, 40]
})

if st.checkbox("Show Data"):
    st.write(df)

st.divider()

options = ["Cat", "Dog", "Fish", "Turtle"]
pet = st.radio("Select your favorite pet:", options)

st.write(f"🐾 Your favorite pet: **{pet}**")

pet_default = st.radio("Pick a pet (fish selected by default):", options, index=2)

st.radio("Favorite Pet (with key):", options, key="fav_pet")
st.write("Session state value:", st.session_state.fav_pet)

st.divider()

cities = ["London", "Berlin", "Paris", "Madrid"]
city = st.selectbox("Select your city:", cities)

st.write(f"🌆 You live in: **{city}**")

city_default = st.selectbox("Pick a city (Berlin selected by default):", cities, index=1)



