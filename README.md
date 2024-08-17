# SpaceX Falcon 9 Launch Analysis & Prediction

## 🚀 Project Overview

This project delves into the world of SpaceX Falcon 9 launches, aiming to analyze historical data and predict the success of future missions using advanced classification models. From data collection to predictive analysis, this project covers the entire data science pipeline.

### Executive Summary

- **Data Collection**: Successfully gathered data from the SpaceX API and through web scraping.
- **Data Wrangling**: Cleaned the dataset for missing values and added a `Class` column to indicate launch success (1) or failure (0).
- **Exploratory Data Analysis (EDA)**: Executed SQL queries and effectively visualized the data.
- **Interactive Visualization**: Developed interactive visualizations using Folium maps and Plotly Dash.
- **Predictive Analysis**: Determined that the Decision Tree model outperformed other models with the highest accuracy.

## 📖 Introduction

### Project Background and Context

The objective of this project is to collect and analyze data to gain insights into the success of SpaceX Falcon 9 launches. The journey starts with gathering data from multiple sources, followed by data wrangling to clean and prepare the data for analysis. 

I explored the data using SQL and visualized relationships between key variables. By segmenting the data and applying statistical analysis, deeper patterns were uncovered. The final step involved building and refining predictive models to understand what drives successful launches, with the findings presented in a clear and compelling manner.

### Problems Addressed

1. How can I efficiently collect and clean data on space launches?
2. What insights can be gained through SQL queries and data visualization?
3. Which predictive model best forecasts launch success?
4. How can I effectively present my analysis?

## 🔬 Methodologies

### Data Collection

- **Historical Data Gathering**: I collected historical data on Falcon 9 and Falcon Heavy launches using the SpaceX API for detailed mission information and web scraping from Wikipedia for additional details.

### Data Wrangling

- **Cleaning and Structuring**: This involved importing the dataset, inspecting its structure, checking for missing values, and ensuring correct data types. I analyzed various features like launch sites, orbit types, and mission outcomes, labeling each launch as either successful or unsuccessful.

### Exploratory Data Analysis (EDA)

- **Visualization & SQL**: Conducted EDA using SQL queries and visualized the data to uncover relationships between variables.

### Interactive Visual Analytics

- **Folium & Plotly Dash**: Created interactive visualizations to explore and present data insights using Folium for maps and Plotly Dash for other visual elements.

### Predictive Analysis

- **Classification Models**: Built and fine-tuned classification models using GridSearchCV to find the best parameters. The models were evaluated based on accuracy and confusion matrix analysis to determine how well they classified the data.

## 📊 Results

### Exploratory Data Analysis (EDA)

- **Launch Sites**: CCAFS LC-40 emerged as the most active launch site, showing a mix of successes and failures.
- **Payload Mass & Booster Performance**: NASA (CRS) missions had a combined payload of 45,596 kg.
- **Success Rates by Orbit & Flight**: Higher flight numbers correlated with increased landing success, while higher payloads often led to positive outcomes.

### Predictive Analysis

- **Mission Success Prediction**: The "Class" column was used to predict launch success.
- **Model Performance**: The Decision Tree model outperformed others, delivering the highest accuracy in predicting successful launches.

### Plotly Dash Visualizations

- **Pie Chart**: KSC LC-39A boasts the highest launch success rate, accounting for 41.7% of total successful launches.
- **Scatter Plot**: The highest success rate was observed for a payload of 5300 kg within the Booster Version Category, specifically when payloads ranged between 2000 and 7000 kg.
