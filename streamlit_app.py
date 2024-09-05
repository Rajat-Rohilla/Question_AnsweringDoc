import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Lab1", "Lab2"], index=1)  # Setting 'Lab2' as default with index=1

# Logic to display the appropriate page
if page == "Lab1":
    st.title("Welcome to Lab 1")
    st.write("This is the content for Lab 1.")
elif page == "Lab2":
    st.title("Welcome to Lab 2")
    st.write("This is the default page (Lab 2).")
