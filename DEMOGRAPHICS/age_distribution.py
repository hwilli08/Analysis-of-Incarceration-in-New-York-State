#This script will read the dataset and plot a histogram showing the distribution of ages among incarcerated individuals.

#Importing necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Filtering data for snapshot year 2023.
data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Calculating age statistics.
mean_age = data_2023['Current Age'].mean()
mode_age = data_2023['Current Age'].mode().values[0]
min_age = data_2023['Current Age'].min()
max_age = data_2023['Current Age'].max()

#Plotting age distribution for snapshot year 2023.
plt.figure(figsize=(12, 6))
plt.hist(data_2023['Current Age'], bins=30, color='#8B4513', edgecolor='black')
plt.axvline(mean_age, color='red', linestyle='--', label=f'Mean Age: {mean_age:.2f}')
plt.axvline(mode_age, color='green', linestyle='--', label=f'Mode Age: {mode_age}')
plt.axvline(min_age, color='blue', linestyle='--', label=f'Min Age: {min_age}')
plt.axvline(max_age, color='purple', linestyle='--', label=f'Max Age: {max_age}')
plt.title('Age Distribution of Incarcerated Individuals in NYS (2023)')
plt.xlabel('Age of Incarcerated Individual')
plt.ylabel('Frequency')
plt.xticks(range(17, 95, 5))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('age_distribution_2023.png')
plt.show()