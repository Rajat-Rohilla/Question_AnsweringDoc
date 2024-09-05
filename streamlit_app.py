# Chatgpt 4.0 mini powered document Answesering 
import openai
from openai import OpenAI
import streamlit as st

lab1 = st.Page("LAB1", title="First lab")
lab2 = st.Page("LAB2", title="Second lab",default=True)

pg= st.navigation([lab1,lab2])
pg.run
