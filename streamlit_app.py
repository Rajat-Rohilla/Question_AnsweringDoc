import openai
from openai import OpenAI
import streamlit as st
import fitz 

# Function to validate the OpenAI API key
def validate_api_key(api_key):
    try:
        client = OpenAI(api_key=api_key)
        response = client.models.list()
        if response:
            return True, client
        else:
            return False, "Failed to validate the API Key."
    except openai.error.AuthenticationError:
        return False, "Invalid API Key. Please check your key and try again."
    except Exception as e:
        return False, f"An error occurred: {e}"


#Function to validate the filetype
def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# Show title and description.
st.title("📄 Document Questioning")
st.write(
    "Upload any file – Answer on tips powered by ChatGPT 4.0 mini.",
    "If you don't have an API Key, create one [here](https://platform.openai.com/account/api-keys)."
)

# Ask user for their OpenAI API key via st.text_input.
openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    is_valid, client_or_error = validate_api_key(openai_api_key)
    
    if is_valid:
        st.success("API Key is valid!")
        
        # Proceed with the rest of the app logic

        document = None

        uploaded_file = st.file_uploader(
            "Upload a document (File)", type=[
                ".txt",  # Plain Text File
                ".pdf",  # PDF   
            ]
        )

        if uploaded_file is not None:
                   file_extension = uploaded_file.name.split('.')[-1]
                   if file_extension == 'txt':
                    document = uploaded_file.read().decode()
                   elif file_extension == 'pdf':
                    document = read_pdf(uploaded_file)
                   else:
                    st.error("Unsupported file type.")
                    

                   if st.checkbox("Show/Hide document content"):
                    st.write(document)
        else:
                    document = None
                    st.write("No File Uploaded or File Removed")
        
        if document is None:
          st.write("No document data available.")

        question = st.text_area(
            "Now ask a question about the document!",
            placeholder="Can you give me a short summary?",
            disabled=not uploaded_file,
        )
        
        if uploaded_file and question:
            messages = [
                {
                    "role": "user",
                    "content": f"Here's a document: {document}---{question}",
                }
            ]
            
            stream = client_or_error.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                stream=True,
            )
            
            st.write_stream(stream)
    else:
        st.error(client_or_error)
else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
