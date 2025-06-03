# display_data_app.py

import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="📊 Displaying Data in Streamlit",
    page_icon="🧪"
)

# Title
st.title("📊 Hello Streamlit World! :smile:")

# Write simple data
st.write("We are learning Streamlit!")

# Lists and Dictionaries
my_list = [1, 2, 3]
st.write("List:", my_list)

my_dict = dict(zip(my_list, ["A", "B", "C"]))
st.write("Dictionary:", my_dict)

# DataFrame
df = pd.DataFrame({
    "First Column": [1, 2, 3, 4],
    "Second Column": [10, 20, 30, 40]
})
st.write("DataFrame (st.write):", df)

# Interactive Table
st.dataframe(df)

# Static Table
st.table(df)

# Emoji Examples
st.write("Streamlit is fun! :rocket: :star2:")
