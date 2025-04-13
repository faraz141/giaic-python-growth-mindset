# 🧹 Data Sweeper

**Data Sweeper** is a user-friendly Streamlit web application that allows you to upload, clean, visualize, and convert datasets in CSV or Excel format. It is ideal for quick data exploration and basic preprocessing.

## 🚀 Features

- 📁 Upload multiple CSV and Excel files.
- 👀 Preview the first few rows of each file.
- 🧼 Clean data by:
  - Removing duplicate rows.
  - Filling missing values in numeric columns with their mean.
- 📊 Select and filter specific columns to work with.
- 📈 Visualize the first two numeric columns using bar charts.
- 🔄 Convert files to CSV or Excel format and download them.

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) - Python framework for building interactive web apps.
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis library.
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Excel file handling for `.xlsx` support.

## 🧪 Requirements

Make sure you have the following installed:

```bash
pip install streamlit pandas openpyxl
