import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt 
import numpy as np
from navigation import make_sidebar

make_sidebar()

# Import the dataset
image = "CGHPI.png"

# Define module content
modules = {
    "MODULE ONE: LEADERSHIP AND GOVERNANCE": """
Leadership Capacity focuses on capacity functions that are typically the responsibility of senior leadership and executive board members (in the case of nonprofits) to guide or execute. Markers of effective organizational leadership include:

- **Vision and Mission**: An organization’s vision and mission statements articulate its sense of purpose and direction. Effective vision and mission statements set parameters for what the organization will and will not do, inspire stakeholders, and set the basis for strategy.
- **Leadership and Governance**: An organization’s governance model is a critical component for organizational functioning and sustainability. For nonprofits with executive boards, clear separation between the board and the organization’s leadership is important, as are documented roles and responsibilities.
- **Strategy and Planning**: An organization’s vision and mission establish its aspirations, but its strategy articulates the means for achieving those goals. Research has shown that strategic planning boosts organizational capacity.
- **Culture and Values**: Organizational culture affects every aspect of functioning – from leadership interactions to responses to challenges. Building a strong, values-based culture must be led and modeled by organizational leadership. Critical components include cultural competency, diversity, equity, and inclusion.

**Suggested Respondents**: Organizational leadership, board members, management, technical leaders, and administrative leaders.
""",
    "MODULE TWO: PROGRAM MANAGEMENT": """
Program implementation is more effective and sustainable if it is well-planned, documented, monitored, and well-coordinated. Key aspects include:

- Policy and procedure manuals provide evidence of a structured, step-by-step approach to programming and serve as essential knowledge and risk management tools.
- Coordination across functional teams or interagency programs reduces inefficiencies and ensures programs do not operate in isolation.
- Performance management focuses on the ability to identify, collect, and monitor key performance indicators directly related to service provision.

**Suggested Respondents**: Project/Program Director, Program/Project Manager, Program/Project Coordinator, Program/Project Advisor, Monitoring and Evaluation Advisor.
""",
    "MODULE THREE: TECHNICAL ASSISTANCE": """
This module assesses the organization’s experience in providing direct or mentorship support for sustainable, high-quality health service delivery. Key aspects include:

- Designing evidence-based programs, monitoring and supporting quality implementation, and making course corrections as needed.
- Understanding and documenting relevant community and individual-level needs and assets through strategies like community needs assessment, asset mapping, and stakeholder focus groups.

**Suggested Respondents**: Technical Director, Technical Advisor, CQI Advisor, and other health advisors.
""",
    "MODULE FOUR: DATA USE/CONTINUOUS QUALITY IMPROVEMENT": """
This module evaluates the organization’s ability to effectively collect, manage, analyze, and utilize data to inform decision-making and strategy. Key components include:

- **Data Collection Protocols**: Clear protocols identify who collects what data, when, from whom, and for what purpose.
- **Measuring Impact**: Using validated tools to assess outcomes and align with service interventions and objectives.
- **Continuous Quality Improvement (CQI)**: Organizations that leverage evaluation findings and link the evaluation process to decision-making demonstrate better improvement and adaptability.

**Suggested Respondents**: Technical Director, Technical Advisor, CQI Advisor, Data Analyst.
""",
    "MODULE FIVE: SUSTAINABILITY": """
This module evaluates the organization’s capacity for long-term viability and resilience. Key aspects include:

- Maintaining consistent, high-quality care amidst changing healthcare landscapes, financial pressures, and evolving patient needs.
- Strategies and innovations to ensure effective, efficient, and patient-centered care.

**Suggested Respondents**: Leadership team, technical teams.
"""
}


# Streamlit application
def app():
    # Main page content


    title = f'Sustainable Capacity of Local Organizations to Reach and End the HIV/AIDS Pandemic (SCORE)'
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(image, width=300)

    st.markdown(f"<h2 style='text-align: center'>{title}</h2>", unsafe_allow_html=True)
    

     # Display each module in a structured format
    for module, content in modules.items():
        st.markdown(f"### {module}")
        st.markdown(content)

                            
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
