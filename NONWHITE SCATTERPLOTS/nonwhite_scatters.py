#This script generates scatter plots comparing the percentage of non-white incarcerated individuals to the total number of incarcerated individuals by housing facility and county in the snapshot year 2023.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by housing facility and counting the number of incarcerated individuals.
facility_counts = incarcerated_data_2023.groupby('Housing Facility').size().reset_index(name='Total_Count')

#Calculating the number of non-white individuals for each housing facility.
nonwhite_counts = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] != 'WHITE'].groupby('Housing Facility').size().reset_index(name='Nonwhite_Count')

#Merging the total counts and non-white counts by housing facility.
facility_counts = pd.merge(facility_counts, nonwhite_counts, on='Housing Facility', how='left')

#Calculating the percentage of non-white individuals for each housing facility.
facility_counts['Nonwhite_Percentage'] = (facility_counts['Nonwhite_Count'] / facility_counts['Total_Count']) * 100

#Creating a scatter plot between the percentage of non-white incarcerated individuals and the total number of incarcerated individuals in the facilities.
plt.figure(figsize=(10, 7))
plt.scatter(facility_counts['Total_Count'], facility_counts['Nonwhite_Percentage'], color='brown', alpha=0.5)  # Axes switched
plt.xlabel('Number of Incarcerated Individuals', fontsize=12)  
plt.ylabel('% Non-White Individuals', fontsize=12)  
plt.title('Total # of Incarcerated Individuals vs. % Non-White by Housing Facility (2023)', fontsize=14)  # Axes switched
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('total_vs_nonwhite_by_facility.png')
plt.show()

#Creating a scatter plot between the percentage of non-white incarcerated individuals and the total number of incarcerated individuals in the facilities.
plt.figure(figsize=(10, 7))
plt.scatter(facility_counts['Nonwhite_Percentage'], facility_counts['Total_Count'], color='brown', alpha=0.5)  # Axes switched
plt.ylabel('Number of Incarcerated Individuals', fontsize=12)  
plt.xlabel('% Non-White Individuals', fontsize=12)  
plt.title('% Non-White vs. Total # of Incarcerated Individuals by Housing Facility (2023)', fontsize=14)  # Axes switched
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('nonwhite_vs_total_by_facility.png')
plt.show()