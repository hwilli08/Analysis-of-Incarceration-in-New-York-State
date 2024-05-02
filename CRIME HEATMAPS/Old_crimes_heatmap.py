#This script analyzes the relationship between the top 10 crimes and both the top 25 correctional facilities (i.e., jails and prisons) and race/ethnicity of incarcerated individuals in 2023, visualizing the data using heatmaps.

#Importing libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the dataset.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Filtering data for the year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Geting the top 25 correctional facilities with the most incarcerated individuals.
top_facilities = incarcerated_data_2023.groupby('Housing Facility').size().nlargest(25).index

#Filtering the dataset to include only the top 25 correctional facilities.
incarcerated_data_2023 = incarcerated_data_2023[incarcerated_data_2023['Housing Facility'].isin(top_facilities)]

#Counting the number of incarcerated individuals by most serious crime.
crime_counts = incarcerated_data_2023['Most Serious Crime'].value_counts().reset_index()
print(crime_counts.head(10))

#Defining the top 10 crimes based on printed list.
top_crimes = [crime_counts.head(10)]

#Filtering the dataset to include only the top 10 crimes.
incarcerated_data_2023 = incarcerated_data_2023[incarcerated_data_2023['Most Serious Crime'].isin(top_crimes)]

#Grouping by correctional facility and crime.
facility_crime_counts = incarcerated_data_2023.groupby(['Housing Facility', 'Most Serious Crime']).size().unstack(fill_value=0)

#Plotting a heatmap for relationship between correctional facility and crime.
plt.figure(figsize=(12, 8))
sns.heatmap(facility_crime_counts, cmap='YlOrBr', annot=True, fmt='d')
plt.title('Relationship between Top 10 Most Serious Crimes Committed and Top 25 NYS Jails/Prisons (2023)')
plt.xlabel('Most Serious Crime')
plt.ylabel('Jail, Prison, or Correctional Facility')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('crime_facility_heatmap_top10.png')
plt.show()

#Grouping by race and crime.
race_crime_counts = incarcerated_data_2023.groupby(['Race/Ethnicity', 'Most Serious Crime']).size().unstack(fill_value=0)

#Plotting a heatmap for relationship between race and crime.
plt.figure(figsize=(12, 8))
sns.heatmap(race_crime_counts, cmap='YlOrBr', annot=True, fmt='d')
plt.title('Relationship between Top 10 Most Series Crimes Committed and Race/Ethnicity of Incarcerated Individuals(2023)')
plt.xlabel('Most Serious Crime')
plt.ylabel('Race/Ethnicity')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('crime_race_heatmap_top10.png')
plt.show()
