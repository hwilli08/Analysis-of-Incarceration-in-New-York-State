#This script generates variation plots showing the difference from the average percentage of non-white individuals in 2023, by County of Indictment and Housing Facility in New York State, with dot sizes corresponding to the number of incarcerated individuals.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by County of Indictment and counting the number of incarcerated individuals.
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Total_Count')

#Calculating the number of non-white individuals for each County of Indictment.
nonwhite_counts = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] != 'WHITE'].groupby('County of Indictment').size().reset_index(name='Nonwhite_Count')

#Merging the total counts and non-white counts by County of Indictment.
county_counts = pd.merge(county_counts, nonwhite_counts, on='County of Indictment', how='left')

#Calculating the percentage of non-white individuals for each County of Indictment.
county_counts['Nonwhite_Percentage'] = (county_counts['Nonwhite_Count'] / county_counts['Total_Count']) * 100

#Calculating the average percentage of non-white individuals across all counties.
average_nonwhite_percentage_county = county_counts['Nonwhite_Percentage'].mean()

#Calculating the difference from the average for each County of Indictment.
county_counts['Difference_from_Average'] = county_counts['Nonwhite_Percentage'] - average_nonwhite_percentage_county

#Creating a variation plot showing the difference from the average by County of Indictment.
plt.figure(figsize=(12, 8))
plt.scatter(county_counts['Difference_from_Average'], county_counts['County of Indictment'], s=county_counts['Total_Count']/10, color='#8B4513')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--', label='Average')  # Adding a vertical line at x=0 for reference
plt.axvline(0, color='red', linewidth=0.5, linestyle='--', label='Average Percentage: {:.2f}%'.format(average_nonwhite_percentage_county))  # Adding a vertical line at the average percentage
#Highlighting counties with more than 40% difference and labeling them.
for index, row in county_counts.iterrows():
    if abs(row['Difference_from_Average']) > 40:
        plt.text(row['Difference_from_Average'], row['County of Indictment'], row['County of Indictment'], fontsize=8, color='red', ha='right' if row['Difference_from_Average'] > 0 else 'left')
plt.xlabel('Difference from Average % Non-White Individuals', fontsize=12)
plt.ylabel('County of Indictment', fontsize=12)
plt.title('Variation of % Non-White Individuals by NYS County of Indictment (2023)', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks([])
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('variation_nonwhite_by_county.png')
plt.show()

#Grouping by Housing Facility and counting the number of incarcerated individuals.
facility_counts = incarcerated_data_2023.groupby('Housing Facility').size().reset_index(name='Total_Count')

#Calculating the number of non-white individuals for each correctional facility.
nonwhite_counts_facility = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] != 'WHITE'].groupby('Housing Facility').size().reset_index(name='Nonwhite_Count')

#Merging the total counts and non-white counts by correctional facility.
facility_counts = pd.merge(facility_counts, nonwhite_counts_facility, on='Housing Facility', how='left')

#Calculating the percentage of non-white individuals for each correctioonal facility.
facility_counts['Nonwhite_Percentage'] = (facility_counts['Nonwhite_Count'] / facility_counts['Total_Count']) * 100

#Calculating the average percentage of non-white individuals across all facilities.
average_nonwhite_percentage_facility = facility_counts['Nonwhite_Percentage'].mean()

#Calculating the difference from the average for each facility.
facility_counts['Difference_from_Average'] = facility_counts['Nonwhite_Percentage'] - average_nonwhite_percentage_facility

#Creating a variation plot showing the difference from the average by facility.
plt.figure(figsize=(12, 8))
plt.scatter(facility_counts['Difference_from_Average'], facility_counts['Housing Facility'], s=facility_counts['Total_Count']/10, color='#8B4513')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--', label='Average')  # Adding a vertical line at x=0 for reference
plt.axvline(0, color='red', linewidth=0.5, linestyle='--', label='Average Percentage: {:.2f}%'.format(average_nonwhite_percentage_facility))  # Adding a vertical line at the average percentage
# Highlighting facilities with more than 30% difference and labeling them.
for index, row in facility_counts.iterrows():
    if abs(row['Difference_from_Average']) > 30:
        plt.text(row['Difference_from_Average'], row['Housing Facility'], row['Housing Facility'], fontsize=8, color='red', ha='right' if row['Difference_from_Average'] > 0 else 'left')
plt.xlabel('Difference from Average % Non-White Individuals', fontsize=12)
plt.ylabel('Jail, Prison, Corrrectional Facility', fontsize=12)
plt.title('Variation of % Non-White Individuals by NYS Jail/Prison (2023)', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks([])
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('variation_nonwhite_by_facility.png')
plt.show()
