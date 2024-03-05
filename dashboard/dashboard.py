import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("dashboard\day.csv")

# Data preprocessing
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Sidebar for selecting analysis
analysis_choice = st.sidebar.selectbox(
    "Choose Analysis:",
    ("Perbedaan Pola Penggunaan Sepeda", "Korelasi antara Kondisi Cuaca dan Jumlah Peminjaman Sepeda",
     "Perbandingan Jumlah Peminjaman Sepeda antara Musim Panas dan Musim Dingin",
     "Tren Harian Jumlah Peminjaman Sepeda")
)

# Analysis based on user selection
if analysis_choice == "Perbedaan Pola Penggunaan Sepeda":
    # Description
    st.markdown("This analysis compares bike rentals based on working day and holiday.")
    # Plot bike rentals based on working day and holiday
    st.header("Perbedaan Pola Penggunaan Sepeda antara Hari Kerja dan Hari Libur")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_df, x='workingday', y='cnt', hue='holiday')
    plt.title('Bike Rentals: Working Day vs Holiday')
    plt.xlabel('Working Day (1: Yes, 0: No)')
    plt.ylabel('Total Bike Rentals')
    plt.xticks(ticks=[0, 1], labels=['Non-Working Day', 'Working Day'])
    plt.legend(title='Holiday', labels=['No', 'Yes'])
    st.pyplot(fig)

elif analysis_choice == "Korelasi antara Kondisi Cuaca dan Jumlah Peminjaman Sepeda":
    # Description
    st.markdown("This analysis examines the correlation between weather conditions and bike rentals.")
    # Plot bike rentals based on weather condition
    st.header("Korelasi antara Kondisi Cuaca dan Jumlah Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_df, x='weather_cond', y='cnt')
    plt.title('Effect of Weather on Bike Rentals')
    plt.xlabel('Weather Condition')
    plt.ylabel('Total Bike Rentals')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif analysis_choice == "Perbandingan Jumlah Peminjaman Sepeda antara Musim Panas dan Musim Dingin":
    # Description
    st.markdown("This analysis compares bike rentals between summer and winter seasons.")
    # Plot bike rentals based on season
    st.header("Perbandingan Jumlah Peminjaman Sepeda antara Musim Panas dan Musim Dingin")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_df, x='season', y='cnt')
    plt.title('Comparison of Bike Rentals: All Seasons')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    st.pyplot(fig)

elif analysis_choice == "Tren Harian Jumlah Peminjaman Sepeda":
    # Description
    st.markdown("This analysis shows the daily trend of bike rental counts over two years.")
    # Plot daily bike rental counts over two years
    st.header("Tren Harian Jumlah Peminjaman Sepeda selama Dua Tahun")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=day_df, x='dteday', y='cnt')
    plt.title('Daily Bike Rental Counts Over Two Years')
    plt.xlabel('Date')
    plt.ylabel('Count of Bike Rentals')
    st.pyplot(fig)
