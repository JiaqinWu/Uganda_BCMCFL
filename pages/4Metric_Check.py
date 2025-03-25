import streamlit as st
import pandas as pd
from navigation import make_sidebar

make_sidebar()

# Load data and image
df = pd.read_csv('Metric.csv')
image = "CGHPI.png"

# Function to render a simple and clean static table without index
def display_static_styled_table(df):
    styled_table = df.style.set_table_styles([
        {'selector': 'th, td',
         'props': [('border', '1px solid #ddd'), ('padding', '10px'), ('text-align', 'left')]},
        {'selector': 'tbody tr:nth-child(even)',
         'props': [('background-color', '#f9f9f9')]},
        {'selector': 'th',
         'props': [('font-weight', 'bold'), ('text-align', 'left')]}
    ]).hide(axis="index")
    st.markdown(styled_table.to_html(index=False), unsafe_allow_html=True)

# Main app function
def app():

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, width=300)

    st.markdown("<h2 style='text-align:center;'>Check the Metrics for Each Question</h2>", unsafe_allow_html=True)

    # Sidebar selection
    st.sidebar.title('Enter Your Selections Here!')
    module_selected = st.sidebar.selectbox('Select Module', df['Module'].unique())
    part_selected = st.sidebar.selectbox('Select Section', df[df['Module'] == module_selected]['Section'].unique())

    st.sidebar.success(f"You selected: {part_selected}")

    # Data filtering based on selections
    filtered_data = df[(df['Module'] == module_selected) & (df['Section'] == part_selected)]

    # Prepare data for display
    records = filtered_data.rename(columns={
        '1: Nonexistent': '1: Nonexistent',
        '2: Basic': '2: Basic',
        '3: Adequate': '3: Adequate',
        '4: Comprehensive': '4: Comprehensive',
        '5: Exceptional': '5: Exceptional'
    })[['Question', '1: Nonexistent', '2: Basic', '3: Adequate', '4: Comprehensive', '5: Exceptional']]

    # Display filtered records
    st.markdown(f"### Metrics for questions within **{module_selected} ➜ {part_selected}**:")
    display_static_styled_table(records)

if __name__ == "__main__":
    app()
