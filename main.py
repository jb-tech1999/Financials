import streamlit as st
import pandas as pd
from io import StringIO
import data_cleansing as dc


st.set_page_config(layout="wide")
st.title('Financial Dashboard')


col1, col2 = st.columns(2)

container = st.container()

try:
    df_melted = st.session_state.df_melted
    #add year filter
    years = df_melted['Year'].unique()

    #multiple select
    year = st.multiselect('Select Year', years)

    #if no year is selected then select max year
    if len(year) == 0:
        year = [max(years)]

    #filter the data
    df_melted = df_melted[df_melted['Year'].isin(year)]
    st.dataframe(df_melted[['Category','Sub-Category','Date','Amount']])


except:
    st.write('Upload a file')




