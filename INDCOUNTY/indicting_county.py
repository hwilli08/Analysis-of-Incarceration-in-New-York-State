#This script generates stacked bar charts demonstrating the racial distribution of incarcerated individuals in New York state in the snapshot year 2023 by indicting county.

#Importing the necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by county of indictment and count the number of incarcerated individuals.
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Total_Count')

#Sorting the counties by count in descending order.
county_counts = county_counts.sort_values(by='Total_Count', ascending=False)

#Calculating the number of incarcerated individuals by race for each county.
racial_counts_by_county = incarcerated_data_2023.groupby(['County of Indictment', 'Race/Ethnicity']).size().unstack(fill_value=0)

#Joining the racial data with the total count by county.
county_counts = county_counts.merge(racial_counts_by_county, on='County of Indictment')

#Plotting stacked bar charts for top 10 and bottom 5 counties. 
#Plotting top 10 counties.
top_10_counties = county_counts.head(10)
if not top_10_counties.empty:
    top_10_counties.set_index('County of Indictment').drop(columns='Total_Count').plot(kind='bar', stacked=True, figsize=(10, 8), color=['#BC8F8F', '#A0522D', '#CD853F', '#D2691E', '#8B5A2B', 'tan'])
    plt.title('Racial Distribution of Incarcerated Individuals in Top 10 Indicting Counties in NYS (2023)', fontsize=12)
    plt.xlabel('Indicting Counties with the Highest Amount of Incarcerated Individuals in NYS', fontsize=12)
    plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
    plt.legend(title='Race/Ethnicity')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    #Adding data labels above the bars.
    for i, total_count in enumerate(top_10_counties['Total_Count']):
        plt.text(i, total_count, str(total_count), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('top_10_counties_race_distribution.png')
    plt.show()

#Plotting bottom 5 counties.
bottom_5_counties = county_counts.tail(5)
if not bottom_5_counties.empty:
    bottom_5_counties.set_index('County of Indictment').drop(columns='Total_Count').plot(kind='bar', stacked=True, figsize=(10, 8), color=['#BC8F8F', '#A0522D', '#CD853F', '#D2691E', '#8B5A2B', 'tan'])
    plt.title('Racial Distribution of Incarcerated Individuals in Bottom 5 Indicting Counties in NYS (2023)', fontsize=12)
    plt.xlabel('Indicting Counties with the Lowest Amount of Incarcerated Individuals in NYS', fontsize=12)
    plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
    plt.legend(title='Race/Ethnicity')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    #Adding data labels above the bars.
    for i, total_count in enumerate(bottom_5_counties['Total_Count']):
        plt.text(i, total_count, str(total_count), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('bottom_5_counties_race_distribution.png')
    plt.show()

#Grouping by county of indictment and counting the number of incarcerated individuals.
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Total_Count')

#Calculating the number of non-white individuals for each county.
nonwhite_counts_by_county = incarcerated_data_2023[incarcerated_data_2023['Race/Ethnicity'] != 'WHITE'].groupby('County of Indictment').size().reset_index(name='Nonwhite_Count')

#Merging the total counts and non-white counts by county.
county_counts = pd.merge(county_counts, nonwhite_counts_by_county, on='County of Indictment', how='left')

#Calculating the percentage of non-white individuals for each county.
county_counts['Nonwhite_Percentage'] = (county_counts['Nonwhite_Count'] / county_counts['Total_Count']) * 100

#Saving the county counts and percentages to a CSV file.
county_counts.to_csv('nonwhite_county_counts.csv', index=False)
