import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt 
import numpy as np
from navigation import make_sidebar

make_sidebar()
 

# Import the dataset
image = "CGHPI.png"


# Streamlit application
def app():
    # Main page content
    title = 'Guidance for this dashboard'

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(image, width=300)

    st.markdown(f"<h2 style='text-align: center'>{title}</h2>", unsafe_allow_html=True)

    st.markdown("""
    ### 1. Metric Check

    Use this tab to review the metrics used to score each question. Select the module and section through the selection bar to view the metrics for each module.
    """)

    st.markdown("""
    ### 2. Score Filtering

    This tab is designed for institutions to filter questions based on the scores of interest. Select the institution name and the score(s) you are interested in.
    """)

    st.markdown("""
    ### 3. Section Analysis

    This tab allows for section analysis. Select the institution, module, and section you want to review to easily see the performance of the questions within that section. If you're curious about scores within a certain range, you can also select those scores in the selection bar.
    """)

    
if __name__ == "__main__":
    app()