import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
st.title('Financial Dashboard')

container = st.container()


col1, col2 = st.columns(2)

df_melted = st.session_state.df_melted
# add year filter
years = df_melted['Year'].unique()

catagories = df_melted['Category'].unique()



with container:
    # multiple select
    with st.sidebar:
        year = st.multiselect('Select Year', years)
        catagory = st.multiselect('Select Catagory', catagories)
    


    # if no year is selected then select max year
    if len(year) == 0:
        year = [max(years)]
    df_melted = df_melted[df_melted['Year'].isin(year)]

    if len(catagory) == 0:
        catagory = catagories

    df_melted = df_melted[df_melted['Category'].isin(catagory)]

    sub_catagories = df_melted['Sub-Category'].unique()
    with st.sidebar:
        sub_catagory = st.multiselect('Select Sub-Catagory', sub_catagories)

    if len(sub_catagory) == 0:
        sub_catagory = sub_catagories

    # filter the data
    
    
    df_melted = df_melted[df_melted['Sub-Category'].isin(sub_catagory)]
    with col1:
        # card with total amount
        total_amount = df_melted['Amount'].sum()
        st.metric(label='Total Amount', value=f'R {round(total_amount,2)}', )

    with col2:
        # month with the highest amount
        df_totals = df_melted.groupby(['Date'])['Amount'].sum()
        max_amount = df_totals.max()
        max_amount_date = df_totals.idxmax()
        # change date format
        max_amount_date = max_amount_date.strftime('%B %Y')

        st.metric(label='Month with highest amount',
                  value=f'{max_amount_date} - R {round(max_amount,2)}', )

    # barchart with totals per month
    with container:
        df_totals = df_melted.groupby(['Date'])['Amount'].sum()
        st.bar_chart(df_totals)
        # barchart with totals per category
        with col1:
            df_totals = df_melted.groupby(['Category'])['Amount'].sum()
            st.bar_chart(df_totals)

        with col2:
            df_totals = df_melted.groupby(['Sub-Category'])['Amount'].sum()
            st.bar_chart(df_totals)
