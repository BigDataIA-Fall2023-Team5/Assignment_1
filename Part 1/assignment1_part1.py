import streamlit as st
import pandas as pd
import numpy as np
from pypdf import PdfReader
from io import BytesIO
import requests


selected_tab = st.sidebar.selectbox("Select a tab:", ["Try", "Docs"])

if selected_tab == "Try":
    try:
        # Code that may raise an exception
        st.title('PDF Document Reader')
        user_url_input = st.text_input("Extract a file", "")
        extraction_method = st.selectbox("Choose Extraction Method", ["PyPDF", "Nougat OCR"])

        if extraction_method == "PyPDF":
            response = requests.get(user_url_input)

            if response.status_code == 200:
            # Open the PDF content as a binary stream
                pdf_stream = BytesIO(response.content)
                pdf_file = PdfReader(pdf_stream)

            # Loop through each page in the PDF
                for page_num in range(len(pdf_file.pages)):
                    # Extract text from the current page
                    page = pdf_file.pages[page_num]
                    page_text = page.extract_text()
                    st.write(page_text)
            else:
                print(f"Failed to retrieve PDF from URL: {response.status_code}")
        
        elif extraction_method == "Nougat OCR":
            st.write("Yet to add this")

    except Exception as e:
        # Handle the exception
        st.write("Enter URL Above")

elif selected_tab == "Docs":
    st.title("Docs Content")
    st.write("This is the content for Docs")










