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
    "Organization Type": """The Baylor College of Medicine Children’s Foundation- Lesotho (BCMCFL) was formed in 2005 as a non-governmental organization resulting from a public-private partnership between the Baylor College of Medicine International Paediatrics AIDS Initiative (BIPAI) in Houston, Texas, USA and the Lesotho Ministry of Health. 

The Comprehensive High Impact Community-Based HIV Prevention, Testing and Treatment Initiation for Sustained Epidemic Control in Lesotho PEPFAR (CoHIP SEC) Project is a five-year project (2022 September – 2027 September) funded by Centers for Disease Control and Prevention (CDC) implemented by BCMCFL. The Project operates in 4 districts; Berea, Leribe, Quthing and Qacha’s Nek targeting adolescents and young people (AYP), men, children and at risk population.""",
    "Baseline Assessment Date": "12 December 2024"
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