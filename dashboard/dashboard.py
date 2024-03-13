import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data():
    day_url = 'https://raw.githubusercontent.com/kusumowidi/Bike-sharing-Dicoding-Project/main/data/day.csv'
    day_df = pd.read_csv(day_url)
    return day_df

day_df = load_data()

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

# Remove infinite values from 'count' column
day_df.replace([np.inf, -np.inf], np.nan, inplace=True)
day_df.dropna(subset=['count'], inplace=True)

# Plot lineplot without infinite values
sns.lineplot(data=day_df, x='dateday', y='count', ax=ax)

ax.set_title('Daily Bike Rental Counts Over Two Years')
ax.set_xlabel('Date')
ax.set_ylabel('Count of Bike Rentals')
st.pyplot(fig)
