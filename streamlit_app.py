# Chatgpt 4.0 mini powered document Answesering 
import openai
from openai import OpenAI
import streamlit as st

LAB1 = st.Page("LAB1", title="First lab")
LAB2 = st.Page("LAB2", title="Second lab",default=True)

pg = st.navigation([LAB1,LAB2])
pg.run()
