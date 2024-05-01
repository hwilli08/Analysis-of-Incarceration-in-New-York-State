#This script generates stacked bar charts demonstrating the racial distribution of incarcerated individuals in New York state in the snapshot year 2023 by facility (i.e., jail, prison, etc.)

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by correctional facility and counting the number of incarcerated individuals.
facility_counts = incarcerated_data_2023.groupby('Housing Facility').size().reset_index(name='Total_Count')

#Calculating the number of incarcerated individuals by race for each facility.
racial_counts_by_facility = incarcerated_data_2023.groupby(['Housing Facility', 'Race/Ethnicity']).size().unstack(fill_value=0)

#Joining the racial data with the total count by facility.
facility_counts = facility_counts.merge(racial_counts_by_facility, on='Housing Facility')

#Sorting facilities by total count in descending order.
facility_counts = facility_counts.sort_values(by='Total_Count', ascending=False)

#Plotting stacked bar charts for top 10 and bottom 10 correctional facilities. 
#Plotting the top 10 facilities.
top_10_facilities = facility_counts.head(10)
if not top_10_facilities.empty:
    top_10_facilities.set_index('Housing Facility').drop(columns='Total_Count').plot(kind='bar', stacked=True, figsize=(10, 8), color=['#BC8F8F', '#A0522D', '#CD853F', '#D2691E', '#8B5A2B', 'tan'])
    plt.title('Racial Distribution of Incarcerated Individuals in Top 10 Jails/Prisons in NYS (2023)', fontsize=14)
    plt.xlabel('Jails/Prisons with the Highest Amount of Incarcerated Individuals in NYS', fontsize=12)
    plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
    plt.legend(title='Race/Ethnicity')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    #Adding data labels above the bars.
    for i, total_count in enumerate(top_10_facilities['Total_Count']):
        plt.text(i, total_count, str(total_count), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('top_10_facilities_race_distribution.png')
    plt.show()

#Plotting the bottom 10 facilities.
bottom_10_facilities = facility_counts.tail(10)
if not bottom_10_facilities.empty:
    bottom_10_facilities.set_index('Housing Facility').drop(columns='Total_Count').plot(kind='bar', stacked=True, figsize=(10, 8), color=['#BC8F8F', '#A0522D', '#CD853F', '#D2691E', '#8B5A2B', 'tan'])
    plt.title('Racial Distribution of Incarcerated Individuals in Bottom 10 Jails/Prisonsin NYS (2023)', fontsize=14)
    plt.xlabel('Jails/Prisons with the Least Amount of Incarcerated Individuals in NYS', fontsize=12)
    plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
    plt.legend(title='Race/Ethnicity')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    #Adding data labels above the bars.
    for i, total_count in enumerate(bottom_10_facilities['Total_Count']):
        plt.text(i, total_count, str(total_count), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('bottom_10_facilities_race_distribution.png')
    plt.show()

#Calculating the number of non-white individuals for each facility.
nonwhite_counts = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] != 'WHITE'].groupby('Housing Facility').size().reset_index(name='Nonwhite_Count')

#Merging the total counts and non-white counts by facility.
facility_counts = pd.merge(facility_counts, nonwhite_counts, on='Housing Facility', how='left')

#Calculating the percentage of non-white individuals for each facility.
facility_counts['Nonwhite_Percentage'] = (facility_counts['Nonwhite_Count'] / facility_counts['Total_Count']) * 100

#Saving the facility counts and percentages to a CSV file.
facility_counts.to_csv('nonwhite_facility_counts.csv', index=False)
