import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
day_df = pd.read_csv("/content/day.csv")

# Title of the dashboard
st.title('Bike Rental Analysis')

# Sidebar with options
st.sidebar.title('Options')
analysis_choice = st.sidebar.selectbox('Choose Analysis', ['Overview', 'Rentals by Month', 'Weather Effect', 'Season Comparison'])

# Data overview
if analysis_choice == 'Overview':
    st.header('Dataset Overview')
    st.write(day_df.head())

# Rentals by month
elif analysis_choice == 'Rentals by Month':
    st.header('Rentals by Month')
    rental_by_month = day_df.groupby('month').agg({'count': 'sum'}).reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=rental_by_month, x='month', y='count', ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Rentals')
    ax.set_title('Total Rentals by Month')
    st.pyplot(fig)

# Weather effect
elif analysis_choice == 'Weather Effect':
    st.header('Effect of Weather on Bike Rentals')
    weather_effect = day_df.groupby('weather_cond').agg({'count': 'mean'}).reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=weather_effect, x='weather_cond', y='count', ax=ax)
    ax.set_xlabel('Weather Condition')
    ax.set_ylabel('Average Rentals')
    ax.set_title('Average Rentals by Weather Condition')
    st.pyplot(fig)

# Season comparison
elif analysis_choice == 'Season Comparison':
    st.header('Seasonal Comparison of Bike Rentals')
    season_comparison = day_df.groupby('season').agg({'count': 'mean'}).reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=season_comparison, x='season', y='count', ax=ax)
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Rentals')
    ax.set_title('Average Rentals by Season')
    st.pyplot(fig)
