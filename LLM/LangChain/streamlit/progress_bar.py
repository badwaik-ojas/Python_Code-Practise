import streamlit as st
import time

# Status message at the top
st.write("🔄 Starting an extensive computation...")

# Create a placeholder for iteration update
latest_iteration = st.empty()

# Create the progress bar
progress_text = "⏳ Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

# Simulate a long computation
for i in range(100):
    # Update progress bar
    my_bar.progress(i + 1, text=progress_text)
    
    # Update status text with current iteration
    latest_iteration.text(f"Iteration {i + 1}")
    
    # Simulate computation delay
    time.sleep(0.1)

# Final message
st.write("✅ We are done! 🎉")
