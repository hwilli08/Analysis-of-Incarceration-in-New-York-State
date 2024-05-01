#This script analyzes trends in incarceration security levels over time in New York State (NYS) and visualizes the distribution of incarcerated individuals across different security levels using line and pie charts, respectively.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

#Reading the dataset.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Standardizing the values in the "Facility Security Level" column.
incarcerated_data['Facility Security Level'] = incarcerated_data['Facility Security Level'].replace('MEDIUM  SECURITY', 'MEDIUM SECURITY')

#Regrouping by year and security level.
yearly_security_level_counts = incarcerated_data.groupby(['Snapshot Year', 'Facility Security Level']).size().unstack(fill_value=0)

#Plotting security level trends over time.
plt.figure(figsize=(12, 8))
yearly_security_level_counts.plot(marker='o', linestyle='-', ax=plt.gca(), color=['#8B4513', 'tan', 'black', '#D2691E', '#8B5A2B'])
plt.title('Incarceration Security Level Trends in NYS (2008-2023)')
plt.xlabel('Year')
plt.ylabel('Number of Incarcerated Individuals')
plt.legend(title='Housing Security Level')
plt.grid(True)
plt.tight_layout()
plt.savefig("security_level_trends.png")
plt.show()

#Printing the counts of each facility type.
facility_counts = yearly_security_level_counts.sum().reset_index()
print("Counts of Each Facility Type:")
print(tabulate(facility_counts, headers=["Facility Security Level", "Count"], tablefmt="grid"))

#Creating a pie chart for security level.
plt.figure(figsize=(12, 8))
security_level_shares = yearly_security_level_counts.sum()
plt.pie(security_level_shares, labels=None, autopct='%1.1f%%', colors=['#8B4513', 'tan', 'black', '#D2691E', '#8B5A2B'])
plt.title('Incarceration Security Level Shares in NYS (2008-2023)')
plt.axis('equal')
plt.legend(security_level_shares.index, loc='center left', bbox_to_anchor=(0.85, 0.5))
plt.savefig("security_level_pie.png")
plt.show()
