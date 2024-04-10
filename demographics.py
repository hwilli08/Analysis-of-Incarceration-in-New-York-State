##This script computes and displays summary statistic information about the demographics of incarcerated individuals in New York State in the snapshot year 2023.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset for incarcerated individuals under custody
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

# Trim down to year 2023
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

# Grouping by indicting county and calculating demographic statistics
# Current Age
age_demographics = incarcerated_data_2023.groupby('County of Indictment')['Current Age'].describe()
age_demographics = age_demographics[['mean', '50%', 'min', 'max']]  # Selecting mean, median (50%), min, and max
age_demographics = age_demographics.rename(columns={'mean': 'Mean', '50%': 'Median', 'min': 'Min', 'max': 'Max'})
# Gender
gender_demographics = incarcerated_data_2023.groupby('County of Indictment')['Gender'].value_counts().unstack(fill_value=0)
gender_counts = incarcerated_data_2023['Gender'].value_counts()
male_ratio = gender_counts['MALE'] / gender_counts.sum()
female_ratio = gender_counts['FEMALE'] / gender_counts.sum()
# Race
race_demographics = incarcerated_data_2023.groupby('County of Indictment')['Race/Ethnicity'].value_counts().unstack(fill_value=0)
race_counts = incarcerated_data_2023['Race/Ethnicity'].value_counts()
nonwhite_ratio = race_counts.drop('WHITE').sum() / race_counts.sum()
white_ratio = race_counts['WHITE'] / race_counts.sum()

# Saving demographic statistics to CSV file
gender_race_ratios = pd.DataFrame({
    'Gender Ratio (Male to Female)': [male_ratio / female_ratio],
    'Race Ratio (Non-white to White)': [nonwhite_ratio / white_ratio]
})
demographics_data = pd.concat([age_demographics, gender_demographics, race_demographics, gender_race_ratios], axis=1)
demographics_data.index.name = 'County of Indictment'
demographics_data.columns = ['Mean Age', 'Median Age', 'Min Age', 'Max Age', 'Female', 'Male', 'Asian', 'Non-Hispanic Black', 'Hispanic', 'Native American','Non-Hispanic White', 'Other', 'Gender Ratio (Male to Female)', 'Race Ratio (Non-white to White)']
demographics_data.to_csv('demographics_data.csv')

#Plotting pie charts for gender and race distributions.
# Gender distribution pie chart
plt.figure(figsize=(7, 7))
gender_counts = incarcerated_data_2023['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightcoral'])
plt.title('Gender Distribution of Incarcerated Individuals in New York State (2023)')
plt.tight_layout()
plt.savefig('gender_distribution_pie_chart.png')
plt.show()
# Race distribution pie chart
plt.figure(figsize=(7, 7))
race_counts = incarcerated_data_2023['Race/Ethnicity'].value_counts()
plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'lightblue', 'lightyellow', 'lightpink', 'lightgrey'])
plt.title('Race/Ethnicity Distribution of Incarcerated Individuals in New York State (2023)')
plt.tight_layout()
plt.savefig('race_distribution_pie_chart.png')
plt.show()