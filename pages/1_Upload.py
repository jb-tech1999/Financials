import streamlit as st
import pandas as pd
from io import StringIO
import data_cleansing as dc



uploaded_file = st.file_uploader("Upload Discover Statement", type="xlsx")
if uploaded_file is not None:

    #get the file name
    file_name = uploaded_file.name

    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    if file_name.endswith('.csv'):
        # To read file as string:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        df = pd.read_csv(stringio)
        #st.write(df)

    elif file_name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file)
        #st.write(df)

    df_clean = dc.clean_data(df)
    df_clean = dc.fix_dates(df_clean)
    df_melted = dc.melt_data(df_clean)
    df_melted = dc.extract_year(df_melted)

    st.session_state.df_melted = df_melted