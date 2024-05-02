#need a description

#Importing neccessary libraries. 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# Reading the dataset for incarcerated individuals under custody for the year 2023.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

# Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

# Reading Prof Wilcoxen's AI-generated ChatGPT file into a dataframe.
df = pd.read_csv("Prof_Wilcoxen_GPT.csv")

# Renaming the "gpt" column to "category" and convert values to Sentence case.
df.rename(columns={"gpt": "category"}, inplace=True)
df['category'] = df['category'].str.capitalize()

# Checking if the value is "na" and replace it with "other".
df.loc[df['category'].str.lower() == "na", 'category'] = "Other"

# Merging without specifying a specific column.
merged_data = pd.merge(incarcerated_data_2023.assign(key=0), df.assign(key=0), on='key', how='outer').drop('key', axis=1)

# Grouping by the 'category' column and count occurrences of each category.
category_counts = merged_data['category'].value_counts()

# Printing each category and its count.
for category, count in category_counts.items():
    print(f"Category: {category}, Count: {count}")

# Printing the total number of crimes in 2023.
total_crimes = len(merged_data)
print(f"Total number of crimes in 2023: {total_crimes}")

# Print crimes and their counts in a table.
crime_table = pd.DataFrame(category_counts).reset_index()
crime_table.columns = ['Crime Type', 'Count']
print(tabulate(crime_table, headers='keys', tablefmt='grid'))

# Visual Analysis: Bar Chart
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='#8B4513')
plt.title('Number of Incarcerated Individuals in NYS by Crime Type (2023)')
plt.xlabel('Crime Type')
plt.ylabel('Number of Individuals')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, max(category_counts) * 1.1)  # Set y-axis limit to start from zero and add a little buffer
for i, count in enumerate(category_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')
plt.tight_layout()
plt.show()

# Calculate percentages
category_percentages = category_counts / total_crimes * 100

# Visual Analysis: Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(category_percentages, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage Distribution of Incarcerated Individuals in NYS by Crime Type (2023)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()

# Relationship between crime category and top 25 correctional facilities
# Grouping by correctional facility and crime.
facility_crime_counts = merged_data.groupby(['Housing Facility', 'category']).size().unstack(fill_value=0)

# Plotting a heatmap for the relationship between correctional facility and crime.
plt.figure(figsize=(12, 8))
sns.heatmap(facility_crime_counts, cmap='YlOrBr', annot=True, fmt='d')
plt.title('Relationship between Crime Category and Top 25 NYS Jails/Prisons (2023)')
plt.xlabel('Crime Category')
plt.ylabel('Jail, Prison, or Correctional Facility')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Relationship between race/ethnicity and crime category
# Grouping by race/ethnicity and crime.
race_crime_counts = merged_data.groupby(['Race/Ethnicity', 'category']).size().unstack(fill_value=0)

# Plotting a heatmap for the relationship between race/ethnicity and crime category.
plt.figure(figsize=(12, 8))
sns.heatmap(race_crime_counts, cmap='YlOrBr', annot=True, fmt='d')
plt.title('Relationship between Crime Category and Race/Ethnicity of Incarcerated Individuals (2023)')
plt.xlabel('Crime Category')
plt.ylabel('Race/Ethnicity')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
