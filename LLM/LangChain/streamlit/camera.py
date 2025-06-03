import streamlit as st
import pandas as pd
import io
st.header("📷 Camera Input")

camera_photo = st.camera_input("Take a photo")

if camera_photo:
    st.image(camera_photo, caption="📸 Captured Photo")
