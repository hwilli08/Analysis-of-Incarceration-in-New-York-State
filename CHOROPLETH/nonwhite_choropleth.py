##This script generates a chloropleth map of the percent nonwhite incarcerated individuals by indicting county in NYS in the snapshot year 2023.

#Importing necessary libraries.
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt 

#Reading the dataset for incarcerated individuals under custody.
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

#Trimming down to year 2023.
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

#Grouping by county and counting the number of incarcerated individuals.
county_counts = incarcerated_data_2023.groupby('County of Indictment').size().reset_index(name='Total_Count')

#Calculating the number of non-white individuals for each county of indictment.
non_white_counts = incarcerated_data_2023[~incarcerated_data_2023['Race/Ethnicity'].str.upper().isin(['WHITE'])].groupby('County of Indictment').size().reset_index(name='Non_White_Count')

#Merging the total counts and non-white counts by county of indictment.
county_counts = pd.merge(county_counts, non_white_counts, on='County of Indictment', how='left')

#Calculating the percentage of non-white individuals for each county of indictment.
county_counts['Non_White_Percentage'] = (county_counts['Non_White_Count'] / county_counts['Total_Count']) * 100

#Reading the county boundaries GeoPackage file.
county_boundaries = gpd.read_file("NYS_Civil_Boundaries.gpkg")

#Merging county boundaries with county counts.
county_boundaries_with_data = county_boundaries.merge(county_counts, left_index=True, right_index=True)

#Plotting the choropleth map showing the intensity of the percentage of non-white individuals.
plt.figure(figsize=(18, 16))  
county_boundaries_with_data.plot(column='Non_White_Percentage', cmap='OrRd', legend=True, legend_kwds={'label': '% Non-White Incarcerated Individuals'})
plt.title('% Non-White Incarcerated Ind. by Indicting NYS County (2023)')
plt.axis('off')

#Saving the figure.
plt.savefig('percent_nonwhite_choropleth.png')

#Sorting the data by Non_White_Percentage in descending order.
sorted_data = county_boundaries_with_data.sort_values(by='Non_White_Percentage', ascending=False)

# Selecting the top 10 counties with the highest percentage of non-white incarcerated individuals.
top_25_counties = sorted_data.head(25)
# Printing the top 10 counties with their names and non-white percentages.
print(top_25_counties[['NAME', 'Non_White_Percentage']].head((25)))

#Writing the top 10 counties data to a CSV file.
sorted_data.to_csv('percent_nonwhite_sorted_counties.csv', index=False)
