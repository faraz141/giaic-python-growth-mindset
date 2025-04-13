import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set the configuration for the Streamlit page
st.set_page_config(page_title="Data Sweeper", layout='wide')

# Title and description of the app
st.title("🧹 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# File uploader widget to upload multiple CSV or Excel files
uploaded_files = st.file_uploader("📁 Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    # Loop through each uploaded file
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()  # Extract the file extension

        # Load the file based on its extension
        if file_ext == ".csv":
            df = pd.read_csv(file)  # Read CSV file into DataFrame
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)  # Read Excel file into DataFrame
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")  # Show error if file type is not supported
            continue

        # Display file information
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")

        # Show a preview of the first few rows of the file
        st.write("### 👀 Preview of the Data")
        st.dataframe(df.head())

        # Section for data cleaning options
        st.subheader("🧼 Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)  # Create two columns for buttons

            with col1:
                # Button to remove duplicate rows
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)  # Remove duplicate rows
                    st.success("✅ Duplicates removed!")

            with col2:
                # Button to fill missing values with the mean of numeric columns
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns  # Select numeric columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())  # Fill missing values with column mean
                    st.success("✅ Missing values filled with column means.")

        # Section to select specific columns to keep
        st.subheader("📊 Select Columns to Keep")
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]  # Keep only selected columns

        # Optional section to show a bar chart visualization
        st.subheader("📈 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_df = df.select_dtypes(include='number')  # Select numeric columns
            if not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :2])  # Show bar chart for the first two numeric columns
            else:
                st.warning("⚠️ No numeric columns available for visualization.")

        # Section for converting file to CSV or Excel format
        st.subheader("🔄 Conversion Option")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # Button to convert and download the cleaned file
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)  # Convert to CSV
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)  # Convert to Excel
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)  # Reset buffer position

            # Create a download button for the converted file
            st.download_button(
                label=f"📥 Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

# Show success message after all files are processed
st.success("🎉 All files processed successfully!")
