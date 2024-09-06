# Chatgpt 4.0 mini powered document Answesering 
import openai
from openai import OpenAI
import streamlit as st
# Show title and description.
st.title("📄 LAB2")
st.write(
    "Upload the any give file – Answer on tips powered by Chatgpt 4.0 mini", 
    "If you don't have any API Key, create one [here](https://platform.openai.com/account/api-keys).)"
)

# Ask user for their OpenAI API key via st.text_input.
openai_api_key = st.secrets["API_KEY"]

if openai_api_key:
    try:
        # Create an OpenAI client to validate the API key
        client = OpenAI(api_key=openai_api_key)
        
        # Make a test request to check if the API key is valid
        response = client.models.list()
        
        if response:
            st.success("API Key is valid!")
            # Proceed with the rest of the app logic
            uploaded_file = st.file_uploader(
                "Upload a document (File)", type=(".txt",  # Plain Text File
    ".md",   # Markdown Documentation File
    ".rtf",  # Rich Text Format
    ".doc",  # Microsoft Word Document
    ".docx", # Microsoft Word Document (newer format)
    ".pdf",  # Portable Document Format
    ".xls",  # Microsoft Excel Spreadsheet
    ".xlsx", # Microsoft Excel Spreadsheet (newer format)
    ".csv",  # Comma-Separated Values
    ".ods",  # OpenDocument Spreadsheet
    ".sql",  # Structured Query Language Data File
    ".db",   # SQLite Database File
    ".sqlite", # SQLite Database File (alternative extension)
    ".mdb",  # Microsoft Access Database
    ".accdb", # Microsoft Access Database (newer format))
            ))
            
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
                    model="gpt-4o-mini",
                    messages=messages,
                    stream=True,
                )
                
                st.write_stream(stream)
        else:
            st.error("Failed to validate the API Key.")
    except openai.OpenAIError:
        st.error("Invalid API Key. Please check your key and try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")

