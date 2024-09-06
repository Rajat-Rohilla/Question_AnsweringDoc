import openai
import os
import streamlit as st

# Show title and description.
st.title("📄 LAB2")
st.write(
    "Upload any document – Get answers powered by ChatGPT 4.0 mini", 
    "If you don't have an API Key, create one [here](https://platform.openai.com/account/api-keys)."
)

# Ask user for their OpenAI API key via st.text_input.
openai_api_key = os.getenv("API_KEY")

if openai_api_key:
    try:
        # Create an OpenAI client to validate the API key
        client = openai
        
        # Make a test request to check if the API key is valid
        response = client.Model.list()
        
        if response:
            st.success("API Key is valid!")
            
            # Sidebar options
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

            model = "gpt-4" if use_advanced_model else "gpt-4-mini"

            # File uploader and question input
            uploaded_file = st.file_uploader(
                "Upload a document (File)", type=(
                    ".txt", ".md", ".rtf", ".doc", ".docx", ".pdf",
                    ".xls", ".xlsx", ".csv", ".ods", ".sql", ".db",
                    ".sqlite", ".mdb", ".accdb"
                )
            )
            
            if uploaded_file:
                document = uploaded_file.read().decode(errors='ignore')

                # Set up instructions based on selected summary format
                if summary_option == "Summarize in 100 words":
                    instructions = "Please summarize the following document in 100 words."
                elif summary_option == "Summarize in 2 connecting paragraphs":
                    instructions = "Please summarize the following document in 2 connecting paragraphs."
                else:
                    instructions = "Please summarize the following document in 5 bullet points."

                # Prepare messages for the OpenAI API
                messages = [
                    {
                        "role": "user",
                        "content": f"{instructions}\n\n---\n\n{document}",
                    }
                ]
                
                # Generate summary using OpenAI API
                response = client.ChatCompletion.create(
                    model=model,
                    messages=messages
                )
                
                summary = response['choices'][0]['message']['content']
                st.write(summary)
                
        else:
            st.error("Failed to validate the API Key.")
    except openai.OpenAIError:
        st.error("Invalid API Key. Please check your key and try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
