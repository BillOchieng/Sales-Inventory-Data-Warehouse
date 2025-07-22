# Importing required packages
import streamlit as st
import pandas as pd
import numpy as np

# --- Landing Page ---
st.title("Hello, Finance!")
st.write(":grin: This is your first Streamlit finance app")
st.text("Let's get started.")

# --- Widget: Text Input & Button ---
name = st.text_input("Enter your username:")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

# --- Generate Random Finance-Like Data ---
st.subheader("Sample Financial Data")
df = pd.DataFrame(np.random.randn(8, 3), columns=["Q", "P", "R"])
df.index = pd.date_range("2024-01-01", periods=8)

# --- Show Data Table ---
st.dataframe(df.style.highlight_max(axis=0))

# --- Line and Bar Charts ---
st.subheader("Line Chart")
st.line_chart(df)

st.subheader("Bar Chart")
st.bar_chart(df)

# --- Layout for Media or Advanced Section ---
st.subheader("More Features Coming Soon!")
st.info(
    "This section can include uploaded files, KPI cards, filters, or embedded media."
)
