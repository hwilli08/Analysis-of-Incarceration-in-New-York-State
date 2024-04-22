import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

# Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

# Grouping by county of indictment and count the number of incarcerated individuals.
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Count')

# Sort the counties by count in descending order.
county_counts = county_counts.sort_values(by='Count', ascending=False)

# Limiting data to top ten counties.
top_counties = county_counts.head(10)

# Saving the county counts to a CSV file.
county_counts.to_csv('new_indcounty_counts.csv', index=False)

# Creating a bar graph of number of incarcerated individuals under custody in each county.
plt.figure(figsize=(12, 8))
bars = plt.bar(top_counties['County of Indictment'], top_counties['Count'], color='blue')

# Adding data labels to the bars for the top ten counties.
for i, bar in enumerate(bars):
    plt.text(i, bar.get_height() + 100, str(bar.get_height()), ha='center', fontsize=10)

plt.xlabel('County', fontsize=12)
plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
plt.title('Top 10 Counties by Number of Incarcerated Individuals Under Custody in NYS (2023)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig('incar_by_county_top10.png')
plt.show()
