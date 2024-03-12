import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv("/content/day.csv")

# Data Wrangling
# Membersihkan data dengan menghapus kolom yang tidak diperlukan
drop_col = ['instant', 'windspeed']
day_df.drop(labels=drop_col, axis=1, inplace=True)

# Mengubah nama kolom untuk kejelasan
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

# Mengubah angka menjadi keterangan untuk kolom-kolom tertentu
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

# Mengubah tipe data kolom tertentu
day_df['dateday'] = pd.to_datetime(day_df.dateday)
day_df['season'] = day_df.season.astype('category')
day_df['year'] = day_df.year.astype('category')
day_df['month'] = day_df.month.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weather_cond'] = day_df.weather_cond.astype('category')

# Data Exploration
# Menampilkan ringkasan statistik
st.title('Analisis Data Sewa Sepeda')
st.write("## Ringkasan Statistik")
st.write(day_df.describe())

# Heatmap Korelasi
st.write("## Heatmap Korelasi")
fig, ax = plt.subplots(figsize=(10, 8))
correlation_matrix = day_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Penyewaan Sepeda vs. Hari Kerja dan Hari Libur
st.write("## Penyewaan Sepeda: Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='workingday', y='count', hue='holiday', ax=ax)
plt.xlabel('Hari Kerja')
plt.ylabel('Total Penyewaan Sepeda')
plt.xticks(ticks=[0, 1], labels=['Hari Libur', 'Hari Kerja'])
plt.legend(title='Libur', labels=['Tidak', 'Ya'])
st.pyplot(fig)

# Efek Cuaca terhadap Penyewaan Sepeda
st.write("## Efek Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='weather_cond', y='count', ax=ax)
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Total Penyewaan Sepeda')
plt.xticks(rotation=45)
st.pyplot(fig)

# Perbandingan Penyewaan Sepeda: Semua Musim
st.write("## Perbandingan Penyewaan Sepeda: Semua Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_df, x='season', y='count', ax=ax)
plt.xlabel('Musim')
plt.ylabel('Total Penyewaan Sepeda')
st.pyplot(fig)

# Jumlah Penyewaan Sepeda Harian Selama Dua Tahun
st.write("## Jumlah Penyewaan Sepeda Harian Selama Dua Tahun")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=day_df, x='dateday', y='count', ax=ax)
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
