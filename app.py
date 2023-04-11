import streamlit as st
import openai
import os
from PyPDF2 import PdfReader
from text_summarizer.functions import summarize

try:
    openai.api_key = os.getenv('OPENAI_KEY')

    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    st.title("Text Summarizer")

    # Allow user to upload a PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

    if pdf_file is not None:
        # Read the contents of the uploaded PDF file
        pdf_reader = PdfReader(pdf_file)
        input_text = ""
        for page in pdf_reader.pages:
            input_text += page.extract_text()
        
        # Display the extracted text in a text area
        st.text_area(label="PDF Text:", value=input_text, height=250)

        # Summarize the extracted text when the "Submit" button is clicked
        if st.button("Submit"):
            summarize(input_text)

    # Display the summarized text in a text area
    output_text = st.text_area(label="Summarized Text:", value=st.session_state["summary"], height=250)
except:
    st.write('There was an error =(')
