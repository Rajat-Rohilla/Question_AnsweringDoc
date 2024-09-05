import streamlit as st

Lab1_page = st.Page("LAB1.py", title="First lab")
Lab2_page = st.Page("LAB2.py", title="Second lab",default=True)

pg = st.navigation([Lab1_page,Lab2_page])
pg.run()
