#This script analyzes incarcerated individuals' data for 2023 in New York State, conducting visual analyses including bar and pie charts for crime distribution, and heatmaps for the relationship between crime categories, correctional facilities, and race/ethnicity.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

#Reading the dataset for incarcerated individuals under custody for the year 2023.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Reading Prof Wilcoxen's AI-generated ChatGPT file into a dataframe.
df = pd.read_csv("Prof_Wilcoxen_GPT.csv")

#Renaming the "gpt" column to "category" and convert values to Sentence case.
df.rename(columns={"gpt": "category"}, inplace=True)
df['category'] = df['category'].str.capitalize()

#Checking if the value is "na" and replace it with "other".
df.loc[df['category'].str.lower() == "na", 'category'] = "Other"

#Merging without specifying a specific column.
merged_data = pd.merge(incarcerated_data_2023.assign(key=0), df.assign(key=0), on='key', how='outer').drop('key', axis=1)

#Grouping by the 'category' column and count occurrences of each category.
category_counts = merged_data['category'].value_counts()

#Printing the total number of crimes in 2023.
total_crimes = len(merged_data)
print(f"Total number of crimes in 2023: {total_crimes}")

#Printing crimes and their counts in a table.
crime_table = pd.DataFrame(category_counts).reset_index()
crime_table.columns = ['Crime Type', 'Count']
print(tabulate(crime_table, headers='keys', tablefmt='grid'))

#Visual Analysis: Bar Chart
plt.figure(figsize=(10, 6))
bars = category_counts.plot(kind='bar', color='#8B4513')
plt.title('Number of Incarcerated Individuals in NYS by Crime Type (2023)')
plt.xlabel('Crime Type')
plt.ylabel('Number of Incarcerated Individuals')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, max(category_counts))
plt.yticks([])  # Remove y-axis labels
for i, count in enumerate(category_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')
plt.tight_layout()
plt.savefig('crime_type_bar_chart.png')
plt.show()

#Calculating percentages.
category_percentages = category_counts / total_crimes * 100
print(category_percentages)

#Visual Analysis: Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(category_percentages, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=['#8B4513', '#A0522D', '#CD853F', '#D2691E', '#8B5A2B', '#BC8F8F'])
plt.title('Percentage Distribution of Incarcerated Individuals in NYS by Crime Type (2023)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.savefig('crime_type_pie_chart.png')
plt.show()

#Relationship between crime category and top 10 correctional facilities
#Grouping by correctional facility and crime.
top_facilities = incarcerated_data_2023.groupby('Housing Facility').size().nlargest(10).index
facility_crime_counts = merged_data[merged_data['Housing Facility'].isin(top_facilities)].groupby(['Housing Facility', 'category']).size().unstack(fill_value=0)

#Plotting a heatmap for the relationship between correctional facility and crime.
plt.figure(figsize=(14, 10))
sns.heatmap(facility_crime_counts, cmap='YlOrBr', annot=True, fmt='d', cbar=False)
plt.title('Relationship between Crime Category and Top 10 Largest NYS Jails/Prisons (2023)')
plt.xlabel('Crime Category')
plt.ylabel('Jail, Prison, or Correctional Facility')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('crime_and_facilities_heatmap.png')
plt.show()

#Relationship between race/ethnicity and crime category
#Grouping by race/ethnicity and crime.
race_crime_counts = merged_data.groupby(['Race/Ethnicity', 'category']).size().unstack(fill_value=0)

#Plotting a heatmap for the relationship between race/ethnicity and crime category.
plt.figure(figsize=(14, 10))
sns.heatmap(race_crime_counts, cmap='YlOrBr', annot=True, fmt='d', cbar=False)
plt.title('Relationship between Crime Category and Race/Ethnicity of Incarcerated Individuals in NYS (2023)')
plt.xlabel('Crime Category')
plt.ylabel('Race/Ethnicity')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('crime_and_race_heatmap.png')
plt.show()

#Relationship between crime category and indicting counties with the highest number of incarcerated individuals
top_counties = incarcerated_data_2023.groupby('County of Indictment').size().nlargest(10).index
county_crime_counts = merged_data[merged_data['County of Indictment'].isin(top_counties)].groupby(['County of Indictment', 'category']).size().unstack(fill_value=0)

#Plotting a heatmap for the relationship between crime category and indicting counties.
plt.figure(figsize=(14, 10))
sns.heatmap(county_crime_counts, cmap='YlOrBr', annot=True, fmt='d', cbar=False)
plt.title('Relationship between Crime Category and Top 10 Indicting Counties with Highest Incarceration Rates (2023)')
plt.xlabel('Crime Category')
plt.ylabel('Indicting County')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('crime_and_counties_heatmap.png')
plt.show()
