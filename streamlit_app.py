import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Lab1", "Lab2"], index=1)  # Set Lab2 as the default page

# Toggle between different .py files
if page == "Lab1":
    st.title("Lab 1")
    exec(open("LAB1.py").read())  # Executes code from lab1.py
elif page == "Lab2":
    st.title("Lab 2")
    exec(open("LAB2.py").read())  # Executes code from lab2.py


