import openai
from openai import OpenAI
import streamlit as st

# Show title and description.
st.title("📄 My Document question answering")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via st.text_input.
openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
        # Create an OpenAI client to validate the API key
        client = OpenAI(api_key=openai_api_key)
        
        # Make a test request to check if the API key is valid
        response = client.models.list()
        
        if response:
            st.success("API Key is valid!")
            # Proceed with the rest of the app logic
            uploaded_file = st.file_uploader(
                "Upload a document (.txt or .md)", type=("txt", "md")
            )
            
            question = st.text_area(
                "Now ask a question about the document!",
                placeholder="Can you give me a short summary?",
                disabled=not uploaded_file,
            )
            
            if uploaded_file and question:
                document = uploaded_file.read().decode()
                messages = [
                    {
                        "role": "user",
                        "content": f"Here's a document: {document} \n\n---\n\n {question}",
                    }
                ]
                
                stream = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    stream=True,
                )
                
                st.write_stream(stream)
        else:
            st.error("Failed to validate the API Key.")
else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
