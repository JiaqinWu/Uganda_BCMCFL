import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt 
import numpy as np
from navigation import make_sidebar

make_sidebar()

# Import the dataset
image = "CGHPI.png"
df = pd.read_csv('final_uganda.csv', encoding='ISO-8859-1')
df['Description'] = df['Description'].str.replace('Ð', '-', regex=False).str.replace('Õ', "'", regex=False)
df['Comment'] = df['Comment'].str.replace('Ð', '-', regex=False).str.replace('Õ', "'", regex=False) 
#df = pd.read_csv('final_uganda.csv')
df['Module'] = df['Module'].replace('One','One: Leadership and Governance').replace('Two','Two: Program Management').replace('Three','Three: Technical Assistance').replace('Four','Four: Data Use').replace("Five","Five: Sustainability")

# Define conditions and choices for the text labels
conditions = [
    df['Score'] == 1,
    df['Score'] == 2,
    df['Score'] == 3,
    df['Score'] == 4,
    df['Score'] == 5
]
choices = ['Nonexistent', 'Basic', 'Adequate', 'Comprehensive', 'Exceptional']

# Apply conditions and choices
df['Level'] = np.select(conditions, choices, default='Nonexistent')


# Streamlit application
def app():
    # Main page content
    

    title = 'Filter Questions by Score'
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(image, width=300)

    st.markdown(f"<h2 style='text-align: center'>{title}</h2>", unsafe_allow_html=True)
    st.sidebar.title('Enter your selections here!')
    

    # Ensure the Score column is sorted
    sorted_unique_scores = sorted(df['Score'].unique())
    #program_selected = st.sidebar.selectbox('Select Institution', df['Program'].unique())

    # Button to select all questions
    if st.sidebar.button('Select All Scores'):
        st.session_state.scores_selected1 = list(sorted_unique_scores)
    elif 'scores_selected1' not in st.session_state:
        # Reset to the first available question by default if not 'Select All' and if part or module has changed
        st.session_state.scores_selected1 = [sorted_unique_scores[0]]

    scores_selected1 = st.sidebar.multiselect(
        'Select Score(s)',
        sorted_unique_scores,
        default=st.session_state.scores_selected1
    )
    st.session_state.scores_selected1 = scores_selected1

    # Displaying the selected options in the sidebar
    scores_selected11 = [str(score) for score in scores_selected1]
    if scores_selected1:  # Checks if any score is selected
        st.sidebar.markdown(f"#### You selected: {', '.join(scores_selected11)}")
    else:
        st.sidebar.markdown("#### No score selected")

     # Update last viewed module and part
    #st.session_state.last_program = program_selected



    # Filter data based on selections
    filtered_data = df[df['Score'].isin(scores_selected1)]
    filtered_data = filtered_data.sort_values(['Module', 'Part', 'Question'])

    # Display the data
    if not filtered_data.empty:
        filtered_data['Section'] = filtered_data['Part']
        records = filtered_data[['Module', 'Section', 'Question', 'Score', 'Level', 'Description','Comment','module','section','Qn']].sort_values(by=['module','section','Qn'])\
            .reset_index().drop(columns=['index','module','section','Qn'])
        st.markdown(f"#### Questions with Score of {', '.join(scores_selected11)} are shown below:")
        st.dataframe(records)
    else:
        st.write("No data available for the selected criteria.")

if __name__ == "__main__":
    app()