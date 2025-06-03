import streamlit as st
import random

# Create two equal columns
left_col, right_col = st.columns(2)

# Generate random data
data = [random.random() for _ in range(100)]

# Add content to left column
with left_col:
    st.subheader("📈 Line Chart")
    st.line_chart(data)

# Add content to right column
right_col.subheader("🔢 First 10 Values")
right_col.write(data[:10])

st.divider()

import streamlit as st
import random

# Create two equal columns
left_col, right_col = st.columns(2)

# Generate random data
data = [random.random() for _ in range(100)]

# Add content to left column
with left_col:
    st.subheader("📈 Line Chart")
    st.line_chart(data)

# Add content to right column
right_col.subheader("🔢 First 10 Values")
right_col.write(data[:10])
