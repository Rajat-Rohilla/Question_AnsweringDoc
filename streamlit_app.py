import streamlit as st
import openai

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Lab1", "Lab2"], index=1)

# Toggle between Lab1 and Lab2 pages
if page == "Lab1":
    st.title("Lab 1")
    exec(open("LAB1.py").read())  
elif page == "Lab2":
    st.title("Lab 2")
    exec(open("LAB2.py").read())  


