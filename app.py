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

### media stuff and display widgets
##  st.sidebar.title("Navigation")
##  st.image("image url", caption="image description")
##  st.video("url")

# File Uploading and caching topics

upload_file = st.file_uploader("upload a csv", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)


st.title(" Text and Markdown")
st.header("This is a header")
st.subheader(" This a subheader")
st.markdown("**bold**, *italic*, `code`, [link](url)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("what is your name?")
st.text_area("write something..")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruits", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")
