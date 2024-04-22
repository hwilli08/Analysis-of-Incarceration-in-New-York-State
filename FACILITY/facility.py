#This script generates stacked bar charts demonstrating the racial distribution of incarcerated individuals in New York state in the snapshot year 2023 by housing facility.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by housing facility and counting the number of incarcerated individuals.
facility_counts = incarcerated_data_2023.groupby('Housing Facility').size().reset_index(name='Total_Count')

#Calculating the number of incarcerated individuals by race for each facility.
racial_counts_by_facility = incarcerated_data_2023.groupby(['Housing Facility', 'Race/Ethnicity']).size().unstack(fill_value=0)

#Joining the racial data with the total count by facility.
facility_counts = facility_counts.merge(racial_counts_by_facility, on='Housing Facility')

#Sorting facilities by total count in descending order.
facility_counts = facility_counts.sort_values(by='Total_Count', ascending=False)

#Plotting stacked bar charts for top 10 and bottom 10 facilities and saving them.
#Plotting top 10 facilities.
top_10_facilities = facility_counts.head(10)
if not top_10_facilities.empty:
    top_10_facilities.set_index('Housing Facility').drop(columns='Total_Count').plot(kind='bar', stacked=True, figsize=(10, 8), color=['#1f77b4', 'brown', '#2ca02c', '#ff7f0e', 'blue', '#8c564b'])
    plt.title('Racial Distribution of Incarcerated Individuals in Top 10 Facilities in NYS (2023)', fontsize=14)
    plt.xlabel('Housing Facility', fontsize=12)
    plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
    plt.legend(title='Race/Ethnicity')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    #Adding data labels above the bars.
    for i, total_count in enumerate(top_10_facilities['Total_Count']):
        plt.text(i, total_count, str(total_count), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('top_10_facilities_race_distribution.png')
    plt.show()

#Plotting bottom 10 facilities.
bottom_10_facilities = facility_counts.tail(10)
if not bottom_10_facilities.empty:
    bottom_10_facilities.set_index('Housing Facility').drop(columns='Total_Count').plot(kind='bar', stacked=True, figsize=(10, 8), color=['#1f77b4', 'brown', '#2ca02c', '#ff7f0e', 'blue', '#8c564b'])
    plt.title('Racial Distribution of Incarcerated Individuals in Bottom 10 Facilities in NYS (2023)', fontsize=14)
    plt.xlabel('Housing Facility', fontsize=12)
    plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
    plt.legend(title='Race/Ethnicity')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    #Adding data labels above the bars.
    for i, total_count in enumerate(bottom_10_facilities['Total_Count']):
        plt.text(i, total_count, str(total_count), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('bottom_10_facilities_race_distribution.png')
    plt.show()

#Writing facility_counts data to a CSV file.
facility_counts.to_csv('racial_distribution_by_facility_2023.csv', index=False)
