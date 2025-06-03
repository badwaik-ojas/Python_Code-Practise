import streamlit as st
import pandas as pd
import io

st.header("📁 File Uploader")

uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "xlsx"])

if uploaded_file:
    st.write("📄 Uploaded File Info:", uploaded_file)

    if uploaded_file.type == "text/plain":
        stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.text_area("Text File Content", string_data, height=200)

    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    else:  # Assume Excel
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)
