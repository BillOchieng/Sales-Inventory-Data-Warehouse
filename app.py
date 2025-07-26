# streamlit	Core UI/dashboarding framework
# pandas	Data manipulation, CSV handling
# numpy	Random number generation, arrays
# matplotlib	Used for static plotting (st.pyplot)
# plotly	For interactive charts (st.plotly_chart)

# Importing required packages
import streamlit as st
import pandas as pd
import numpy as np

import sqlite3

conn = sqlite3.connect("warehouse.db")
# Use conn to read/write as needed


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

st.text_input("What is your name?")
st.text_area("write something..")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruits", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.button("Click Me"):
    st.success("Button Clicked!")

if st.checkbox("Show Details"):
    st.info("Here are more details..")

option = st.radio("Choose view", ["Show Chart", "Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success(f"welcome, {username}!")

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

col1, col2 = st.columns(2)

with col1:
    st.button("Click me in Column 1")
with col2:
    st.button("Click me in column 2")

with st.expander("See Explanation"):
    st.write("Here is a hidden message inside the expander.")


# st.image("url", caption="Sample Image", use_column_width=True)

# st.videp("url")

# audio_file = open("example.mp3", "rb")
# st.audio(audio_file.read(), format="audio/mp3")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increament"):
    st.session_state.count += 1

st.write("Counter:", st.session_state.count)

import time


# @st.cache_data def slow_function():
#     time.sleep(3)
#     return "Done!"

#
# if st.button("Run slow function"):
#     result = slow_function()
#     st.success(result)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)

import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
