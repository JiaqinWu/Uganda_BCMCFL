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
    "Date": "12 December 2024",
    "Assessment Team": "Martine Etienne-Mesubi, Arnold Mafukidze, Sharon Kibwana",
    "Number of Active Funded Projects": [
        "1. Ministry of Health Subvention: Provides Financial support for all service delivery at 6 Baylor-owned health facilities, including 1 center of excellence",
        "2. Comprehensive High-Impact Community-Based HIV Prevention, Testing, and Treatment Initiation for Sustained Epidemic Control in Lesotho (CoHip-SEC) – CDC",
        "3. Karabo ea Bophelo (KB) – USAID funded, closing January 2025",
        "4. Lesotho/Local Entities Advancing and Driving Health Responses (LEADR) - USAID",
        "5. Protecting Women, Infants & Children From HIV in Lesotho (PINCH) – Global Fund",
        "6. Providing prevention and treatment for young people (PROTECT) – Global Fund",
        "7. Closing TB Gaps for People Living with HIV: TB Guidance for Adaptable Patient Centered Service  TB Gaps) – CDC",
        "8. Serious Fun Children’s Network – Psychosocial programming",
        "9. EGPAF - ???",
    ],
    "Patients on Care": "Approximately 5000 patients across facilities; National TXCURR: 232,000; TA for 28,000 under PEPFAR through LEADR and other grants",
    "Active Donors": "MOH, CDC, USAID, Global Fund, Serious Fun Children’s Network, EGPAF",
    "Number of Staff": "603 total",
    "Paid by Institution": "N/A",
    "Paid by MOH": "143",
    "Paid by PEPFAR": "361 (health workers, community volunteers, and temporary staff)",
    "Paid by Global Fund": "101 (Protect and PINCH projects)",
    "Current Supported Partners": [
        "5 subawards ending December 2024 under the KB Project",
        "Lenephwa – Lesotho Network of People Living with HIV – funded by both CDC and USAID grants"
    ],
    "Supported Health Facilities/Communities": [
        "MOH Subvention funds the Maseru center of excellence and 5 satellite clinics",
        "LEADR project provides TA for 26 sites in two districts"
    ]
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