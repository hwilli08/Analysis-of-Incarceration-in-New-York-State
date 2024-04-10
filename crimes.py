##This script runs an analysis of the most serious crime committed by incarcerated individuals in NYS in snapshot year 2023. It generates a bar graph demonstrating the counts of the top 10 most serious crimes committed and prints lists of the most popular/unpopular most serious crimes.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Counting the number of incarcerated individuals by most serious crime.
crime_counts = incarcerated_data['Most Serious Crime'].value_counts().reset_index()
crime_counts.columns = ['Most Serious Crime Committed by Incarcerated Individual', 'Count']

#Saving the crime counts to CSV file.
crime_counts.to_csv('crime_counts.csv', index=False)

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
plt.savefig('top_crimes.png')
plt.show()

#Getting lists of the top 10 and least 10 reported most serious crimes.
top_10_crimes = crime_counts.head(10)
least_10_crimes = crime_counts.tail(10)

#Writing the top 10 and least 10 reported most serious crimes to CSV
top_10_crimes.to_csv('top_10_crimes.csv', index=False)
least_10_crimes.to_csv('least_10_crimes.csv', index=False)

#Printing the top 10 and least 10 reported most serious crimes.
print("Top 10 Reported Most Serious Crimes:")
print(top_10_crimes)
print("\nLeast 10 Reported Most Serious Crimes:")
print(least_10_crimes)
