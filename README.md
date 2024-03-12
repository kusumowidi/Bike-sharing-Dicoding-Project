# Bike-sharing-Dicoding-Project

# Air Quality Data Analysis with Python - Dicoding Submission
[Air Quality Data Dashboard Streamlit App](https://mnaufalladicoding1.streamlit.app) <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo"></img>

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)

## Overview
This project is a data analysis and visualization project focused on The analysis of bike rental data, encompassing data wrangling, exploration, and visualization. Initial steps involve importing and cleaning the data, followed by exploratory analysis through grouping, aggregation, and correlation analysis. Visualization and explanatory analysis include plotting boxplots to compare rentals between working days and holidays, exploring the influence of weather conditions on rentals, and examining rental trends across seasons and over time. These insights aid in understanding rental patterns and inform decision-making for bike rental businesses.

## Project Structure
- `dashboard/`: This directory contains dashboard.py which is used to create dashboards of data analysis results.
- `data/`: Directory containing the raw CSV data files.
- `Proyek_Analisis_Data.ipynb/`: This file is used to perform data analysis.
- `requirements.txt/`: This file lists all the modules needed.
- `url.txt/`: This file contain the streamlit dashboard url.
- `README.md`: This documentation file.

## Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/kusumowidi/Bike-sharing-Dicoding-Project
```
2. Go to the project directory
```
cd Bike-sharing-Dicoding-Project
```
3. Install the required Python packages by running:
```
pip install -r requirements.txt
```

## Usage
1. **Data Wrangling**:
- Data is imported using Pandas from two CSV files: one for daily data and one for hourly data.
- Data quality is assessed through methods like .info(), .isna(), .duplicated(), and .describe().
- Data cleaning involves dropping unnecessary columns and renaming columns for better understanding. Additionally, some numerical values are mapped to categorical labels.
- Data types are converted to appropriate types like datetime and categorical.

3. **Exploratory Data Analysis (EDA)**: 
- Grouping and aggregation operations are performed to understand patterns based on different features like month, weather condition, holiday, weekday, working day, and season.
- Correlation heatmap is plotted to visualize relationships between numerical features.

5. **Visualization**: Run the Streamlit dashboard for interactive data exploration:

```
cd Proyek_Analisis_Data.ipynb/dashboard
streamlit run dashboard.py
```
Access the dashboard in your web browser at `https://mnaufalladicoding1.streamlit.app`.

## Data Sources
The project uses Air Quality Dataset from [Belajar Analisis Data dengan Python's Final Project](https://drive.google.com/drive/folders/1ZHrg-qiun_CfsKgl3jmgGT49286Ko28/view) offered by [Dicoding](https://www.dicoding.com/).
