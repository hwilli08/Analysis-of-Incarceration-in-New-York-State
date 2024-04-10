#Importing necessary libraries.
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Reading the county boundaries GeoPackage file.
county_boundaries = gpd.read_file("NYS_Civil_Boundaries.gpkg")

#Reading the dataset for incarcerated individuals under custody by county.
incarcerated_data = pd.read_csv("indcounty_counts.csv")

#Merging the percentage data with county boundaries using the county names.
county_map = county_boundaries.merge(incarcerated_data, left_index=True, right_index=True)

#Plotting the original heatmap (percentage of incarcerated individuals in NYS by indicting county).
plt.figure(figsize=(18, 16))
county_map.plot(column='Percentage', cmap='OrRd', legend=True)
plt.title('% Incarcerated Individuals by Indicting NYS County (2023)')
plt.axis('off')
plt.savefig('indictment_chloropleth.png')