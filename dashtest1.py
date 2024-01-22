import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('city.csv')
    return data

data = load_data()

# Streamlit page configuration
st.title('City Data Dashboard')
st.sidebar.title('Navigation')

# Sidebar for city selection
city = st.sidebar.selectbox('Select a city:', data['City'].unique())

# Function to get city data
def get_city_data(city):
    return data[data['City'] == city]

# Display city data
if st.sidebar.button('Show City Data'):
    city_data = get_city_data(city)
    st.write(city_data)

# Plotting function using Plotly
def plot_data(metric):
    fig = px.line(data, x='Month', y=metric, color='City', title=f'{metric} Over Time')
    return fig

# Select metric to plot
metric = st.selectbox('Select metric to compare:', ['Decibel_Level', 'Traffic_Density', 
                                                    'Green_Space_Area', 'Air_Quality_Index', 
                                                    'Happiness_Score', 'Cost_of_Living_Index', 
                                                    'Healthcare_Index'])

# Display plot
if st.button('Show Plot'):
    plot = plot_data(metric)
    st.plotly_chart(plot)

# Run the Streamlit app by saving this script and running `streamlit run your_script_name.py` from your command line.
