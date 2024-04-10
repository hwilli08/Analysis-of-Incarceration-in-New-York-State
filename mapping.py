import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Read the county boundaries CSV file
county_boundaries = gpd.read_file("NYS_Civil_Boundaries.csv")

# Read the dataset for incarcerated individuals under custody
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

# Trim down to year 2023
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

# Group by county of indictment and count the number of incarcerated individuals
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Count')

# Calculate the percentage of total incarcerated individuals in each county
total_count = county_counts['Count'].sum()
county_counts['Percentage'] = (county_counts['Count'] / total_count) * 100

# Merge the percentage data with county boundaries using the county names
county_map = county_boundaries.merge(county_counts, how='left', left_on='NAME', right_on='County of Indictment')

# Replace non-finite values with a default value (e.g., 0)
county_map['Percentage'] = county_map['Percentage'].fillna(0)

# Convert 'Percentage' column to integer
county_map['Percentage'] = county_map['Percentage'].astype(int)

# Plot the heatmap
plt.figure(figsize=(10, 8))
county_map.plot(column='Percentage', cmap='OrRd', legend=True)
plt.title('Percentage of Incarcerated Individuals by County (2023)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()
