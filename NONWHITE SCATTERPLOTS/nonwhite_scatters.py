# This script generates scatter plots comparing the percentage of non-white incarcerated individuals to the total number of incarcerated individuals by housing facility and county in the snapshot year 2023.

# Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

# Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

# Grouping by housing facility and counting the number of incarcerated individuals.
facility_counts = incarcerated_data_2023.groupby('Housing Facility').size().reset_index(name='Total_Count')

# Calculating the number of non-white individuals for each housing facility.
nonwhite_counts = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] != 'WHITE'].groupby('Housing Facility').size().reset_index(name='Nonwhite_Count')

# Merging the total counts and non-white counts by housing facility.
facility_counts = pd.merge(facility_counts, nonwhite_counts, on='Housing Facility', how='left')

# Calculating the percentage of non-white individuals for each housing facility.
facility_counts['Nonwhite_Percentage'] = (facility_counts['Nonwhite_Count'] / facility_counts['Total_Count']) * 100

# Saving the facility counts and percentages to a CSV file.
facility_counts.to_csv('nonwhite_facility_counts.csv', index=False)

# Creating a scatter plot between the percentage of non-white incarcerated individuals and the total number of incarcerated individuals in the facilities.
plt.figure(figsize=(10, 6))
plt.scatter(facility_counts['Total_Count'], facility_counts['Nonwhite_Percentage'], color='brown', alpha=0.5)  # Axes switched
plt.xlabel('Number of Incarcerated Individuals', fontsize=12)  # Axes switched
plt.ylabel('% Non-White Individuals', fontsize=12)  # Axes switched
plt.title('Total # of Incarcerated Individuals vs. % Non-White by Housing Facility (2023)', fontsize=14)  # Axes switched
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('scatterplot_total_vs_nonwhite_by_facility.png')
plt.show()

# Grouping by county and counting the number of incarcerated individuals.
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Total_Count')

# Calculating the number of non-white individuals for each county.
nonwhite_counts_by_county = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] != 'WHITE'].groupby('County of Indictment').size().reset_index(name='Nonwhite_Count')

# Merging the total counts and non-white counts by county.
county_counts = pd.merge(county_counts, nonwhite_counts_by_county, on='County of Indictment', how='left')

# Calculating the percentage of non-white individuals for each county.
county_counts['Nonwhite_Percentage'] = (county_counts['Nonwhite_Count'] / county_counts['Total_Count']) * 100

# Creating a scatter plot between the percentage of non-white incarcerated individuals and the total number of incarcerated individuals by county.
plt.figure(figsize=(10, 6))
plt.scatter(county_counts['Total_Count'], county_counts['Nonwhite_Percentage'], color='brown', alpha=0.5)  # Axes switched
plt.xlabel('Number of Incarcerated Individuals', fontsize=12)  # Axes switched
plt.ylabel('% Non-White Individuals', fontsize=12)  # Axes switched
plt.title('Total # of Incarcerated Individuals vs. % Non-White by County (2023)', fontsize=14)  # Axes switched
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig('scatterplot_total_vs_nonwhite_by_county.png')
plt.show()
