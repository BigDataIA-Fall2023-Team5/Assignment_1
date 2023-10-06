import streamlit as st
import pandas as pd
import numpy as np
from pypdf import PdfReader
from io import BytesIO
import requests
import wget
import os
import re

st.image('Screenshot 2023-10-06 at 1.48.30 AM.png')

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
            target_directory = "/Users/shruti/Desktop/Assignment_1/Part_1"
            
            wget.download(user_url_input, out=target_directory)
            match = re.search(r'/([^/]+)$', user_url_input)
            extracted_part = match.group(1)
            file_path = os.path.join(target_directory, extracted_part)
            url = "https://c041-34-125-116-59.ngrok-free.app/predict"
            payload = {}
            files=[('file',(extracted_part,open(file_path,'rb'),'application/pdf'))]
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            if response.status_code == 200:
                st.write(response.text)
                if os.path.exists(file_path):
                    os.remove(file_path)

            else:
                st.write(f"Failed to retrieve PDF from URL: {response.status_code}")
            
                


    except Exception as e:
        # Handle the exception
        st.write("Enter URL Above")

elif selected_tab == "Docs":
    st.title("DOCUMENTATION FOR NOUGHAT AND PYPDF")
    st.subheader("NOUGHAT PROS AND CONS:")
    st.write("""
             **PROS:**
             - Better handling of images and embedded objects within the PDF
             - Provides more contextual summaries for longer documents
             """)
    st.write("""
             **CONS:**
             - Slower processing time as compared to pypdf
             - Some compatibility issues with heavily formatted documents
             """)
    st.subheader("PYPDF PROS AND CONS:")
    st.write("""
             **PROS:**
             - Faster processing speeds for text-heavy documents
             - Simple to use and has a straightforward integration with Streamlit
             """)
    st.write("""
             **CONS:**
             - Cannot effectively handle images or embedded objects
             - Summaries can occasionally miss crucial information for very lengthy documents
              """)
    st.subheader("ARCHITECTURE DIAGRAM")
    st.image('pdf_reader.png')
