#This script analyzes data on incarcerated individuals in NYS for 2023, counting occurrences of each most serious crime and categorizing them into 10 groups. It generates bar graphs for the top 10 most frequent crimes and the distribution of crimes by type.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Counting the number of incarcerated individuals by most serious crime.
crime_counts = incarcerated_data_2023['Most Serious Crime'].value_counts().reset_index()
crime_counts.columns = ['Most Serious Crime Committed by Incarcerated Individual', 'Count']

#Saving the crime counts to CSV file.
crime_counts.to_csv('total_crime_counts.csv', index=False)

#Creating a bar graph of the top 10 most serious crimes committed.
top_crimes = crime_counts.head(10)
plt.figure(figsize=(10, 6))
bars = plt.bar(top_crimes['Most Serious Crime Committed by Incarcerated Individual'], top_crimes['Count'], color='skyblue')
plt.xlabel('Most Serious Crime Committed', fontsize=12)
plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
plt.title('Top Most Serious Crimes Committed by Incarcerated Individuals in NYS in 2023', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
#Adding data labels.
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20, str(int(bar.get_height())), ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('specific_top_mostseriouscrimes.png')
plt.show()

#Getting lists of the top 10 and least 10 reported most serious crimes.
top_10_crimes = crime_counts.head(10)
least_10_crimes = crime_counts.tail(10)

#Writing the top 10 and least 10 reported most serious crimes to CSV.
top_10_crimes.to_csv('top_10_specific_crimes.csv', index=False)
least_10_crimes.to_csv('least_10_specific_crimes.csv', index=False)

#Printing the top 10 and least 10 reported most serious crimes.
print("Top 10 Reported Most Serious Crimes:")
print(top_10_crimes)
print("\nLeast 10 Reported Most Serious Crimes:")
print(least_10_crimes)

#Defining a function to categorize crime types into 10 specific groups.
def categorize_crime(crime):
    if 'murder' in crime.lower():
        return 'Murder'
    elif 'robbery' in crime.lower():
        return 'Robbery'
    elif 'burglary' in crime.lower():
        return 'Burglary'
    elif 'theft' in crime.lower():
        return 'Theft'
    elif 'assault' in crime.lower():
        return 'Assault'
    elif 'rape' in crime.lower():
        return 'Rape'
    elif 'sexual abuse' in crime.lower():
        return 'Sexual Abuse'
    elif 'drug' in crime.lower():
        return 'Drug Offense'
    elif 'weapon' in crime.lower():
        return 'Weapon Offense'
    else:
        return 'Other'

#Applying the categorization function to create a new column for crime groups.
incarcerated_data_2023['Crime Group'] = incarcerated_data_2023['Most Serious Crime'].apply(categorize_crime)

#Counting the number of incarcerated individuals by crime group.
crime_counts_grouped = incarcerated_data_2023['Crime Group'].value_counts().reset_index()
crime_counts_grouped.columns = ['Crime Group', 'Count']

#Calculating the percentage of each crime group.
total_count_grouped = crime_counts_grouped['Count'].sum()
crime_counts_grouped['Percentage'] = (crime_counts_grouped['Count'] / total_count_grouped) * 100

#Writing the grouped crime count information and percentages into a CSV file.
crime_counts_grouped.to_csv('grouped_crime_counts.csv', index=False)

#Creating a bar graph of the most serious crimes committed, grouped by specific crime types.
plt.figure(figsize=(14, 10))
bars = plt.bar(crime_counts_grouped['Crime Group'], crime_counts_grouped['Count'], color='skyblue')
plt.xlabel('Crime Group', fontsize=12)
plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
plt.title('Most Serious Crimes Committed by Incarcerated Individuals in NYS in 2023 (Grouped by Specific Crime Types)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
#Adding data labels.
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20, str(int(bar.get_height())), ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('grouped_top_crimes.png')
plt.show()
