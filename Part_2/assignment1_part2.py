import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import openpyxl
import great_expectations as ge
from great_expectations.data_context import FileDataContext

# Set Streamlit app title
st.title("Freddie Mac Dataset Quality Assessment App")

# Upload CSV or XLS file
uploaded_file = st.file_uploader("Upload a CSV or XLS file", type=["csv", "xls"])

# User selects data type
data_type = st.radio("Select Data Type:", ("Origination Data", "Monthly Performance Data"))

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    if uploaded_file.type == "application/vnd.ms-excel":
        df = pd.read_excel(uploaded_file, engine="openpyxl")
    else:
        df = pd.read_csv(uploaded_file)
    
    profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
    profile.to_file("output.html")
    with open('output.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    st.components.v1.html(html_content, width=800, height=600)


    if data_type == "Origination Data":
        context = ge.data_context.DataContext("/Users/shruti/Desktop/Assignment_1/Part_2/gx")
        checkpoint_config = context.get_checkpoint("Freddie_Mac_Monthly_v1")
        checkpoint_result = checkpoint_config.run(run_name="Manual_run")
        data = context.build_data_docs()
        link = data['local_site']
        st.write(link)


