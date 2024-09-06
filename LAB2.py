# Chatgpt 4.0 mini powered document Answesering 
import openai
import os
from openai import OpenAI
import streamlit as st
# Show title and description.
st.title("📄 LAB2")
st.write(
    "Upload the any give file – Answer on tips powered by Chatgpt 4.0 mini", 
    "If you don't have any API Key, create one [here](https://platform.openai.com/account/api-keys).)"
)

# Ask user for their OpenAI API key via st.text_input.
openai_api_key = os.getenv("API_KEY")
openai.api_key = openai_api_key

if openai_api_key:
    try:
        # Create an OpenAI client to validate the API key
        client = OpenAI(api_key=openai_api_key)
        
        # Make a test request to check if the API key is valid
        response = client.models.list()
        
        if response:
            st.success("API Key is valid!")

            
            st.sidebar.header("Summary Options")
            summary_option = st.sidebar.radio(
                "Choose summary format:",
                [
                    "Summarize in 100 words",
                    "Summarize in 2 connecting paragraphs",
                    "Summarize in 5 bullet points"
                ]
            )
            
            use_advanced_model = st.sidebar.checkbox("Use Advanced Model (GPT-4)")

            model = "gpt-4" if use_advanced_model else "gpt-4o-mini"

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
            
            if uploaded_file:
                document = uploaded_file.read().decode(errors='ignore')

                # Set up instructions based on selected summary format
                if summary_option == "Summarize in 100 words":
                    instructions = "Please summarize the following document in 100 words."
                elif summary_option == "Summarize in 2 connecting paragraphs":
                    instructions = "Please summarize the following document in 2 connecting paragraphs."
                else:
                    instructions = "Please summarize the following document in 5 bullet points."

                messages = [
                    {
                        "role": "user",
                        "content": f"{instructions}\n\n---\n\n{document}",
                    }
                ]
                
                 # Generate summary using OpenAI API
                response = client.chat.completions.create(
                    model=model,
                    messages=messages
                )
                
                summary = response.choices[0].message.content
                st.write(summary)
                
        else:
            st.error("Failed to validate the API Key.")
    except openai.OpenAIError:
        st.error("Invalid API Key. Please check your key and try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")