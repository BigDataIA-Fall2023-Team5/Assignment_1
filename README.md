# Text Extraction Tool and Freddie Mac Dataset Quality Assessment App on Streamlit

## Assignment_1

## Summary
The project encompasses the development of two distinct tools. <br>
<br>

**Text Extraction Tool** - The first tool helps in summarizing PDF files, particularly from the SEC. Users upload a PDF file onto the streamlit tool, and then choose between two libraries for processing: nougat and pypdf to process and extract. <br>
https://assignment1-4vyy2ltpzhkmc9lvqkbxht.streamlit.app/ <br>
<br>
**Freddie Mac Dataset Quality Assessment App** - The second tool aids in the assessment and validation of datasets from Freddie Mac against the specified schema. It integrates great expectations to validate the data against 99 expectations for both Monthly and Origination data then uses pandasprofiling to provide a comprehensive summary of the uploaded dataset.<br>
https://k4zmnuibfbfjretfv5au69.streamlit.app/<br>
<br>
Both tools will be interactive, web-based applications developed using Streamlit and hosted on Streamlit's public cloud.
<br>
<br>
## Architecture

## File Structure
Part 1: <br>


<br>
Part 2: <br>
Part_2
├── GEX_Monthly
│&nbsp;&nbsp;&nbsp;├── .DS_Store
│&nbsp;&nbsp;&nbsp;├── GEX%20_monthly.ipynb
│&nbsp;&nbsp;&nbsp;└── gx
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── .DS_Store
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── .gitignore
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── great_expectations.yml
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── checkpoints
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── Freddie_Mac_Monthly_v1.yml
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── data
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── .DS_Store
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── expectations
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── .ge_store_backend_id
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── GE_Suite.json
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── plugins
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── custom_data_docs
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── styles
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── data_docs_custom_styles.css
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── custom_data_docs
│
├── GEX_Origination
│   ├── .DS_Store
│   ├── GEX%20_Origination.ipynb
│   └── gx
│       ├── .DS_Store
│       ├── .gitignore
│       ├── great_expectations.yml
│       ├── checkpoints
│       │   ├── Freddie_Mac_Origination_v1.yml
│       │   └── checkpoints
│       ├── data
│       │   ├── .DS_Store
│       │   ├── historical_data_2020.csv
│       │   └── historical_data_2022.csv
│       ├── expectations
│       │   ├── .ge_store_backend_id
│       │   └── GE_Suite.json
│       └── plugins
│           └── custom_data_docs
│               ├── styles
│               │   └── data_docs_custom_styles.css
│               └── custom_data_docs
│
├── streamlit2
│   ├── data_profiling.png
│   ├── main2.py
│   └── requirements.txt
│
├── .DS_Store
├── Readme.md
├── assignment1_part2.py
└── data_profiling.png



**WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK**<br>

Contribution by each member:<br>
  ● Anamika Bharali: 33.3%<br>
  ● Saniya Kapur: 33.3%<br>
  ● Shruti Suresh Mundargi: 33.3%

