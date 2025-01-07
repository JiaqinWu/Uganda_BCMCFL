import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt 
import numpy as np
import re
import plotly.express as px
from navigation import make_sidebar

make_sidebar()

# Import the dataset
image = "CGHPI.png"
#df = pd.read_csv('Metric.csv', encoding='ISO-8859-1')
df = pd.read_csv('Metric.csv')
#df = df.rename(columns={'ï»¿Module':'Module'})
#df.replace({'\n': ' ', '\t': ' '}, regex=True, inplace=True)
#df.replace('âs ',"'s")
           




def display_static_styled_table(df):
    # Define custom CSS
    custom_css = """
    <style>
        .stTable {
            width: 100% !important;
            table-layout: fixed;
        }
        .stTable tbody td {
            text-align: left;
            padding: 8px;
            border:2px solid #ddd;
            word-wrap: break-word;
        }
        .stTable tbody tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
    """
    
    # Display the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    
    # Create a copy of the DataFrame without the index
    df_no_index = df.copy()
    df_no_index.index = [''] * len(df)
    
    # Display the static table
    st.table(df_no_index)

# Streamlit application
def app():
    # Main page content
    #st.set_page_config(page_title = 'Dashboard -- Uganda SCORE Survey', page_icon='🇺🇬',layout='wide')

    title = 'Check the metrics for each question'
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(image, width=300)

    st.markdown(f"<h2 style='text-align: center'>{title}</h2>", unsafe_allow_html=True)
        

    # Sidebar for selection
    st.sidebar.title('Enter your selections here!')
    module_selected1 = st.sidebar.selectbox('Select Module', df['Module'].unique())
    part_selected1 = st.sidebar.selectbox('Select Section', df[df['Module'] == module_selected1]['Section'].unique())
    st.sidebar.markdown(f"#### You selected: {part_selected1}")



    


    # Show data based on selections
    st.markdown(f"#### Metrics for questions within {module_selected1}: {part_selected1} are shown below:")
    # Filter data based on selections
    filtered_data = df[(df['Module'] == module_selected1) & 
                    (df['Section'] == part_selected1)].reset_index()

    #records = filtered_data[['Module', 'Section', 'Question', '1: Nonexistent', '2: Basic','3: Adequate','4: Comprehensive','5: Exceptional']].reset_index().drop(columns='index')
    #st.dataframe(records)
    records = filtered_data.rename(columns={'1: Nonexistent':'1:Nonexistent', '2: Basic':'2:Basic', '3: Adequate': '3:Adequate',\
                                            '4: Comprehensive':'4:Comprehensive','5: Exceptional':'5:Exceptional'})\
        [['Question', '1:Nonexistent', '2:Basic','3:Adequate','4:Comprehensive','5:Exceptional']].reset_index().drop(columns='index')
    #st.dataframe(records)
    #st.table(records)
    display_static_styled_table(records)

if __name__ == "__main__":
    app()