import openai
from openai.error import AuthenticationError
import streamlit as st

# Show title and description.
st.title("📄Document Questioning")
st.write(
    "Upload any file – Get answers instantly powered by ChatGPT 4.0 mini.",
    "If you don't have an API Key, create one [here](https://platform.openai.com/account/api-keys)."
)

# Ask user for their OpenAI API key via st.text_input.
openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    try:
        # Set the OpenAI API key
        openai.api_key = openai_api_key
        
        # Make a test request to check if the API key is valid
        response = openai.Model.list()

        if response:
            st.success("API Key is valid!")
            # Proceed with the rest of the app logic
            uploaded_file = st.file_uploader(
                "Upload a document (File)", 
                type=(".txt", ".md", ".rtf", ".doc", ".docx", ".pdf", ".xls", 
                      ".xlsx", ".csv", ".ods", ".sql", ".db", ".sqlite", 
                      ".mdb", ".accdb")
            )
            
            question = st.text_area(
                "Now ask a question about the document!",
                placeholder="Can you give me a short summary?",
                disabled=not uploaded_file,
            )
            
            if uploaded_file and question:
                document = uploaded_file.read().decode('utf-8')
                messages = [
                    {
                        "role": "user",
                        "content": f"Here's a document: {document} \n\n---\n\n {question}",
                    }
                ]
                
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    stream=True,
                )
                
                for message in response:
                    st.write(message['choices'][0]['delta'].get('content', ''))
        else:
            st.error("Failed to validate the API Key.")
    except AuthenticationError:
        st.error("Invalid API Key. Please check your key and try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
