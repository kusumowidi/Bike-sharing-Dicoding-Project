import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    day_df = pd.read_csv("/content/day.csv")
    return day_df

day_df = load_data()

# Data Cleaning
# Drop unnecessary columns
drop_col = ['instant', 'windspeed']
day_df.drop(columns=drop_col, inplace=True)

# Rename columns
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

# Map numerical values to categorical
day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weather_cond'] = day_df['weather_cond'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

# Convert data types
day_df['dateday'] = pd.to_datetime(day_df['dateday'])
day_df['season'] = day_df['season'].astype('category')
day_df['year'] = day_df['year'].astype('category')
day_df['month'] = day_df['month'].astype('category')
day_df['holiday'] = day_df['holiday'].astype('category')
day_df['weekday'] = day_df['weekday'].astype('category')
day_df['workingday'] = day_df['workingday'].astype('category')
day_df['weather_cond'] = day_df['weather_cond'].astype('category')

# Dashboard
st.title('Bike Rental Data Analysis Dashboard')

# Data Exploration Section
st.header('Data Exploration')

# Displaying the first few rows of the data
st.subheader('Sample of the Dataset')
st.write(day_df.head())

# Summary Statistics
st.subheader('Summary Statistics')
st.write(day_df.describe())

# Correlation Heatmap
st.subheader('Correlation Heatmap')
fig, ax = plt.subplots(figsize=(10,6))
correlation_matrix = day_df.corr()
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".2f",
    ax=ax
)
st.pyplot(fig)

# Data Visualization Section
st.header('Data Visualization')

# Boxplot: Working Day vs Holiday
st.subheader('Bike Rentals: Working Day vs Holiday')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='workingday', y='count', hue='holiday', ax=ax)
ax.set_title('Bike Rentals: Working Day vs Holiday')
ax.set_xlabel('Working Day (1: Yes, 0: No)')
ax.set_ylabel('Total Bike Rentals')
ax.set_xticklabels(['Non-Working Day', 'Working Day'])
ax.legend(title='Holiday', labels=['No', 'Yes'])
st.pyplot(fig)

# Boxplot: Weather Condition vs Bike Rentals
st.subheader('Effect of Weather on Bike Rentals')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='weather_cond', y='count', ax=ax)
ax.set_title('Effect of Weather on Bike Rentals')
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Total Bike Rentals')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Boxplot: Season vs Bike Rentals
st.subheader('Comparison of Bike Rentals: All Seasons')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='season', y='count', ax=ax)
ax.set_title('Comparison of Bike Rentals: All Seasons')
ax.set_xlabel('Season')
ax.set_ylabel('Total Bike Rentals')
st.pyplot(fig)

# Line Plot: Daily Bike Rental Counts Over Two Years
st.subheader('Daily Bike Rental Counts Over Two Years')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=day_df, x='dateday', y='count', ax=ax)
ax.set_title('Daily Bike Rental Counts Over Two Years')
ax.set_xlabel('Date')
ax.set_ylabel('Count of Bike Rentals')
st.pyplot(fig)
