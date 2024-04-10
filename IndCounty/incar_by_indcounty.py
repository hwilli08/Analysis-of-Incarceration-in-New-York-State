##This script generates a bar graph demonstrating the number of incarcerated individuals in New York state in the snapshot year 2023 by indicting county.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt 

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by county of indictment and count the number of incarcerated individuals.
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Count')

#Calculating the percentage of total incarcerated individuals in each county.
total_count = county_counts['Count'].sum()
county_counts['Percentage'] = (county_counts['Count'] / total_count) * 100

#Identifying the indicting counties with the highest number of incarcerated individuals.
top_counties = county_counts.nlargest(5, 'Count')

#Saving the county counts and percentages to a CSV file.
county_counts.to_csv('indcounty_counts.csv', index=False)

#Creating a bar graph of number of incarcerated individuals under custody in each county.
plt.figure(figsize=(12, 8))
bars = plt.bar(county_counts['County of Indictment'], county_counts['Count'])
#Changing the color of bars for the counties with the highest number of incarcerated individuals.
for bar in bars:
    if bar.get_height() in top_counties['Count'].values:
        bar.set_color('red')
#Adding data labels to the bars for the top five counties.
for i, bar in enumerate(bars):
    if bar.get_height() in top_counties['Count'].values:
        plt.text(i, bar.get_height() + 100, str(bar.get_height()), ha='center', fontsize=10)
plt.xlabel('County', fontsize=12)
plt.ylabel('Number of Incarcerated Individuals', fontsize=12) 
plt.title('Number of Incarcerated Individuals Under Custody in NYS by Indicting County (2023)', fontsize=14) 
plt.xticks(rotation=45, ha='right', fontsize=10) 
plt.tight_layout() 
plt.savefig('incar_by_county.png')