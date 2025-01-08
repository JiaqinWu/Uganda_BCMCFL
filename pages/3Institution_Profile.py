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


# Institutional Profile Data
institution_profile = {
    "Organization Name": "Baylor College of Medicine Children’s Foundation Lesotho (BCMCFL)",
    "Organization Type": "NGO established 19 years ago",
    "Date": "12 December 2024"
}

# Streamlit App
def app():
    # Main Page
    title = "Institutional Profile"
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(image, width=300)

    st.markdown(f"<h2 style='text-align: center'>{title}</h2>", unsafe_allow_html=True)

    # Display Institutional Profile
    for key, value in institution_profile.items():
        st.markdown(f"### {key}")
        if isinstance(value, list):  # Handle lists separately
            for item in value:
                st.markdown(f"- {item}")
        else:
            st.markdown(value)

# Run the app
if __name__ == "__main__":
    app()