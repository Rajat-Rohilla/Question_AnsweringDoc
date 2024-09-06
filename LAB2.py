import openai
import os
import PyPDF2
import streamlit as st

# Show title and description.
st.title("📄 LAB2: Document Question Answering")
st.write(
    "Upload any file – Answer your questions about the document powered by ChatGPT 4.0 mini. "
    "If you don't have an API Key, create one [here](https://platform.openai.com/account/api-keys)."
)

# Ask user for their OpenAI API key via environment variable or input
openai_api_key = os.getenv("API_KEY")

if not openai_api_key:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    openai.api_key = openai_api_key  # Set the API key

    try:
        # Make a test request to check if the API key is valid
        openai.Model.list()  # This checks if the API key is valid
        
        st.success("API Key is valid!")

        # Sidebar options for summary format and model choice
        summary_option = st.sidebar.radio(
            "Choose a summary type:",
            ["Summarize in 100 words", "Summarize in 2 paragraphs", "Summarize in 5 bullet points"]
        )

        use_advanced_model = st.sidebar.checkbox("Use Advanced Model (gpt-4)")

        # File uploader for document
        uploaded_file = st.file_uploader(
            "Upload a document (File)", 
            type=["txt", "md", "rtf", "doc", "docx", "pdf", "xls", "xlsx", "csv", "sql", "db", "sqlite", "mdb", "accdb"]
        )

        # Function to format the OpenAI prompt based on summary selection
        def format_summary_prompt(document, summary_option):
            if summary_option == "Summarize in 100 words":
                return f"Summarize the following document in 100 words:\n\n{document}"
            elif summary_option == "Summarize in 2 paragraphs":
                return f"Summarize the following document in 2 paragraphs:\n\n{document}"
            elif summary_option == "Summarize in 5 bullet points":
                return f"Summarize the following document in 5 bullet points:\n\n{document}"

        if uploaded_file:
            # Handling different file types
            if uploaded_file.type == "application/pdf":
                # Extract text from the PDF file
                reader = PyPDF2.PdfReader(uploaded_file)
                document = "\n".join([page.extract_text() for page in reader.pages])
            else:
                document = uploaded_file.read().decode("utf-8")

            # Format the prompt for OpenAI
            prompt = format_summary_prompt(document, summary_option)

            # Choose the model based on checkbox selection
            model = "gpt-4" if use_advanced_model else "gpt-4o-mini"

            # Send request to OpenAI API
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )

            summary = response.choices[0].message["content"]

            # Display the generated summary
            st.write(summary)

    except openai.error.AuthenticationError:
        st.error("Invalid API Key. Please check your key and try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
