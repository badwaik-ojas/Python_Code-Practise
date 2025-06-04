import streamlit as st

# Display the full session state (works like a dict)
st.write(st.session_state)

st.divider()

# Initialize counter if not in session state
if "counter" not in st.session_state:
    st.session_state["counter"] = 0  # Bracket notation
else:
    st.session_state.counter += 1    # Dot notation

# Display the counter
st.write(f"Counter: {st.session_state.counter}")

st.divider()

# Initialize clicks
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

# Create a button and update clicks on press
if st.button("Update State"):
    st.session_state.clicks += 1

# Show session state after clicking
st.write(f"After pressing button: {st.session_state}")

st.divider()

# Slider value stored in session state under key "my_slider"
number = st.slider("Pick a number", 1, 10, key="my_slider")

# Access value from variable and session state
st.write(f"Number: {number}")
st.write(st.session_state)  # See 'my_slider' key
