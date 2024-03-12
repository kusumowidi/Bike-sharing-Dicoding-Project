import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv("/content/day.csv")

# Data Wrangling
# Drop unnecessary columns
drop_col = ['instant', 'windspeed']
day_df.drop(labels=drop_col, axis=1, inplace=True)

# Rename columns
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

# Map numeric values to categorical values
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
day_df['dateday'] = pd.to_datetime(day_df.dateday)
day_df['season'] = day_df.season.astype('category')
day_df['year'] = day_df.year.astype('category')
day_df['month'] = day_df.month.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weather_cond'] = day_df.weather_cond.astype('category')

# Streamlit App
st.title('Bike Rental Dashboard')

# Display summary statistics
st.write("## Summary Statistics")
st.write(day_df.describe())

# Correlation Heatmap
st.write("## Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 8))
correlation_matrix = day_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Bike Rentals: Working Day vs Holiday
st.write("## Bike Rentals: Working Day vs Holiday")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='workingday', y='count', hue='holiday', ax=ax)
plt.xlabel('Working Day')
plt.ylabel('Total Bike Rentals')
plt.xticks(ticks=[0, 1], labels=['Non-Working Day', 'Working Day'])
plt.legend(title='Holiday', labels=['No', 'Yes'])
st.pyplot(fig)

# Effect of Weather on Bike Rentals
st.write("## Effect of Weather on Bike Rentals")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='weather_cond', y='count', ax=ax)
plt.xlabel('Weather Condition')
plt.ylabel('Total Bike Rentals')
plt.xticks(rotation=45)
st.pyplot(fig)

# Comparison of Bike Rentals: All Seasons
st.write("## Comparison of Bike Rentals: All Seasons")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='season', y='count', ax=ax)
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals')
st.pyplot(fig)

# Daily Bike Rental Counts Over Two Years
st.write("## Daily Bike Rental Counts Over Two Years")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=day_df, x='dateday', y='count', ax=ax)
plt.xlabel('Date')
plt.ylabel('Count of Bike Rentals')
st.pyplot(fig)
