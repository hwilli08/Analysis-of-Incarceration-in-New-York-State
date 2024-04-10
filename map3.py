import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Read the county boundaries GeoPackage file
county_boundaries = gpd.read_file("NYS_Civil_Boundaries.gpkg")
print(county_boundaries.head())

# Read the dataset for incarcerated individuals under custody by county
incarcerated_data = pd.read_csv("indcounty_counts.csv")

# Merge the percentage data with county boundaries using the county names
county_map = county_boundaries.merge(incarcerated_data, how='left', left_on='NAME', right_on='County of Indictment')

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
