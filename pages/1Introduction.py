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


    title = f'Sustainable Capacity of Local Organizations to Reach and End the HIV/AIDS Pandemic (SCORE)'
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(image, width=300)

    st.markdown(f"<h2 style='text-align: center'>{title}</h2>", unsafe_allow_html=True)
    

    st.markdown("""
    ### ACKNOWLEDGEMENT

    The “Sustainable Capacity of Local Organizations to Reach and End the HIV/AIDS Pandemic (SCORE)” Project is funded by the US Centers for Disease Control and Prevention (CDC)/PEPFAR through the global award NU2GGH002503. (September 2023 – September 2028).

    Implemented by Georgetown University (Center for Global Health Practice and Impact, O’Neill Institute for National and Global Health Law, Center for Global Health Science and Security, Department of Global Health, McCourt School of Public Policy, McDonough Business School), and partners Sustainability Solutions and Aspen Institute, the SCORE Project is designed to provide governments, faith-based organizations and community-based organizations with support to sustain HIV and related disease outcome gains and strengthen local capacity for resilient and equitable country health systems. 

    The SCORE Project is designed to provide governments, faith-based organizations, and community-based organizations with support to sustain HIV and related disease outcome gains and strengthen local capacity for resilient and equitable country health systems.

    The SCORE HIV/AIDS Pandemic Organizational and Technical Needs Assessment Tool (SCORE-POT) is designed to assess existing organizational capacity to manage and deliver sustainable HIV programs. The tool reviews six modules:

    1. **Module 1: Governance and Leadership**
    2. **Module 2: Program Management**
    3. **Module 3: Technical Assistance**
    4. **Module 4: Data Use**
    5. **Module 5: Sustainability**
    6. **Module 6: Finance and Administration** - this module was implemented by Sustainability Solutions using the USAID Non-U.S. Organization Pre-Award Survey (NUPAS) tool. Data for this module is not included in this dashboard.

    The SCORE-POT has been developed by the SCORE Project with additions, adaptations and modifications from the USAID Non-U.S. Organization Pre-Award Survey (NUPAS) tool, the PEPFAR Strategic Direction (September 2022), and the Americorps Organizational Assessment Tool, Washington DC (2017), and the PEPFAR Rapid Site-level Health Workforce Assessment Tool.
    """)

    st.markdown("""
    ### INTRODUCTION

    In Uganda, the SCORE Project is providing technical assistance to selected faith-based and community-based organizations to strengthen their organizational, leadership, and management capacities to manage and deliver sustainable HIV programs. The capacity and needs assessment is the first step towards building capacity and is conducted through the use of a standardized process or formal instrument to assess facets of organizational capacity and identify areas of relative strength and weakness.

    Through applying the SCORE Pandemic Organizational and Technical Needs Assessment Tool (SCORE-POT), the Project will collaborate with your organization to assess institutional capacity to implement locally driven innovations to sustain HIV epidemic control, support long-term planning, address emerging challenges, and implement adaptive programming.
    """)
                            
    st.markdown("""
    ### USAGE
    This dashboard is designed to allow audiences to explore and analyze scoring data across different dimensions. Here are the details of the four sub-tabs:

    1. **Tab 1: Institution Profile** - Show the overall institution profile.
    2. **Tab 2: Guidance** - Show the guidance how to use this dashboard.
    3. **Tab 3: Metrics** - Show the metrics for each question when giving a score.
    4. **Tab 4: Score Filtering** - Filter and view questions that meet certain score criteria.
    5. **Tab 5: Section Analysis** - Examine the scores of various questions within a selected section for a specific institution.

    Feel free to explore any tab to interact with the data!
    """)





if __name__ == "__main__":
    app()
