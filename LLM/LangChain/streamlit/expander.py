import streamlit as st
import random

# Create an expander
with st.expander("📊 Click to expand"):
    # Add a bar chart with random data
    data = {
        'Random Data': [random.randint(2, 10) for _ in range(25)]
    }
    st.bar_chart(data)

    # Add an image
    st.write("🐶 Here's a dog:")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
