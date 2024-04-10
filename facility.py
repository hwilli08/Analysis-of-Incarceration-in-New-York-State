##This script generates a bar graph demonstrating the number of incarcerated individuals in New York state in the snapshot year 2023 by housing facility.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt 

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by housing facility and counting the number of incarcerated individuals.
facility_counts = incarcerated_data_2023.groupby('Housing Facility').size().reset_index(name='Total_Count')

#Calculating the number of Black individuals for each housing facility.
black_counts = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] == 'BLACK'].groupby('Housing Facility').size().reset_index(name='Black_Count')

#Merging the total counts and Black counts by housing facility.
facility_counts = pd.merge(facility_counts, black_counts, on='Housing Facility', how='left')

#Calculating the percentage of Black individuals for each housing facility.
facility_counts['Black_Percentage'] = (facility_counts['Black_Count'] / facility_counts['Total_Count']) * 100

#Identifying the housing facilities with the highest percentages of Black individuals.
top_black_facilities = facility_counts.nlargest(5, 'Black_Percentage')

#Identifying the housing facilities with the highest number of incarcerated individuals.
top_facilities = facility_counts.nlargest(5, 'Total_Count')

#Saving the facility counts and percentages to a CSV file.
facility_counts.to_csv('facility_counts.csv', index=False)

#Creating a bar graph of number of incarcerated individuals under custody in each housing facility.
plt.figure(figsize=(14, 10))
bars = plt.bar(facility_counts['Housing Facility'], facility_counts['Total_Count'])
# Changing the color of bars for the facilities with the highest number of incarcerated individuals.
for bar in bars:
    if bar.get_height() in top_facilities['Total_Count'].values:
        bar.set_color('red')
    if bar.get_height() in top_black_facilities['Total_Count'].values:
        bar.set_color('black')
# Adding data labels to the bars for the top five facilities.
for i, bar in enumerate(bars):
    if bar.get_height() in top_facilities['Total_Count'].values:
        plt.text(i, bar.get_height() + 100, str(bar.get_height()), ha='center', fontsize=10)
plt.xlabel('Housing Facility', fontsize=12)
plt.ylabel('Number of Incarcerated Individuals', fontsize=12) 
plt.title('Number of Incarcerated Individuals Under Custody in NYS by Housing Facility (2023)', fontsize=14) 
plt.xticks(rotation=90, ha='center', fontsize=8) 
plt.tight_layout() 
plt.savefig('incar_by_facility.png')
plt.show()

# Creating a bar chart for the top five housing facilities with the highest percentages of Black individuals.
plt.figure(figsize=(10, 6))
plt.bar(top_black_facilities['Housing Facility'], top_black_facilities['Black_Percentage'], color='brown')
plt.xlabel('Housing Facility', fontsize=12)
plt.ylabel('Percentage of Black Individuals', fontsize=12)
plt.title('Top Five Housing Facilities in NYS with Highest Percentage of Black Incarcerated Individuals (2023)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('top_black_facilities.png')
plt.show()