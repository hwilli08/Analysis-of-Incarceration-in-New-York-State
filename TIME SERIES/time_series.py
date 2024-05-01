#This script reads the dataset, groups the data by year, and calculates the count of incarcerated individuals for each year. Then, it creates a time series plot showing the trend of the number of incarcerated individuals over the years from 2008 to 2023.
#The script also creates a time series plot showing the trends in the number of incarcerated individuals over the years, separately for white and non-white individuals, based on the race/ethnicity data in the dataset.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Grouping by year and counting the number of incarcerated individuals each year.
yearly_counts = incarcerated_data.groupby('Snapshot Year').size()
print(yearly_counts)

#Plotting the time series for overall incarcerated individuals.
plt.figure(figsize=(12, 8))
yearly_counts.plot(marker='o', color='black', linestyle='-', label='Overall')
plt.title('Number of Incarcerated Individuals in NYS (2008-2023)')
plt.xlabel('Year')
plt.ylabel('Total Number of Incarcerated Individuals')
plt.legend()
plt.grid(True)
for i, txt in enumerate(yearly_counts):
    plt.annotate(txt, (yearly_counts.index[i], yearly_counts.values[i]), textcoords="offset points", xytext=(0,10), ha='center')
#Setting the x-axis limits to include 2023.
plt.xlim(2008, 2023) 
#Ensuring all years from 2008 to 2023 are labeled.
plt.xticks(range(2007, 2025))
plt.tight_layout()
plt.savefig('timeseries_total_incarcerated_individuals.png')
plt.show()

#Grouping by year and race/ethnicity and counting the number of incarcerated individuals each year.
yearly_race_counts = incarcerated_data.groupby(['Snapshot Year', 'Race/Ethnicity']).size().unstack(fill_value=0)

#Grouping all other racial groups into "Non-White".
yearly_race_counts['Non-White'] = yearly_race_counts.drop(columns='WHITE').sum(axis=1)

#Plotting the time series for white and nonwhite individuals.
plt.figure(figsize=(12, 8))
yearly_race_counts['WHITE'].plot(marker='o', color='tan', linestyle='-', label='White')
yearly_race_counts['Non-White'].plot(marker='o', color='#8B4513', linestyle='-', label='Non-White')
plt.title('Number of Incarcerated Individuals in NYS by Race (2008-2023)')
plt.xlabel('Year')
plt.ylabel('Number of Incarcerated Individuals')
plt.legend()
plt.grid(True)
for i, txt in enumerate(yearly_race_counts['WHITE']):
    plt.annotate(txt, (yearly_race_counts.index[i], yearly_race_counts['WHITE'].values[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(yearly_race_counts['Non-White']):
    plt.annotate(txt, (yearly_race_counts.index[i], yearly_race_counts['Non-White'].values[i]), textcoords="offset points", xytext=(0,10), ha='center')
#Setting the x-axis limits to include 2023.
plt.xlim(2008, 2023) 
#Ensuring all years from 2008 to 2023 are labeled.
plt.xticks(range(2007, 2025))
plt.tight_layout()
plt.savefig('timeseries_race_incarcerated_individuals.png') 
plt.show()
