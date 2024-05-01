# Analysis of Incarcerated Individuals in New York State

This repository houses a comprehensive analysis of incarcerated individuals' demographics, trends, facilities, and crimes in New York State for the year 2023. It includes scripts written in Python for data processing, visualization, and interpretation. The analysis covers a wide range of aspects, including age, gender, race, time series trends, facility distribution, indicting county demographics, variation from average non-white percentages, choropleth mapping, and crime statistics. Each script is meticulously documented, detailing its purpose and methodology. The provided visualizations offer clear insights into the distribution and characteristics of the incarcerated population, aiding policymakers, researchers, and the public in understanding and addressing issues related to incarceration, demographics, and criminal justice in New York State. This repository serves as a valuable resource for further research, policymaking, and advocacy efforts aimed at improving the criminal justice system and addressing disparities within it.

## Input Data Sources
- [Incarcerated Individuals Under Custody Beginning 2008](https://data.ny.gov/Public-Safety/Incarcerated-Individuals-Under-Custody-Beginning-2/55zc-sp6m/about_data)

This core dataset provides comprehensive information on individuals under custody in New York State, starting from 2008. It encompasses data on demographics, crimes committed, and facility details, offering insights into trends and patterns within the state's criminal justice system over time. 

- [NYS Civil Boundaries](https://data.gis.ny.gov/datasets/sharegisny::nys-civil-boundaries/explore?layer=2&location=42.846702%2C-78.687173%2C7.82&showTable=true)

By providing detailed geographical boundaries of administrative units such as counties, cities, towns, and villages within New York State, this dataset enables the creation of accurate and informative choropleth maps that depict various socio-demographic characteristics, including the distribution of incarcerated individuals by indicting county. Choropleth maps created using this dataset allow for the visualization of regional disparities in incarceration rates, demographic composition, and other relevant factors, facilitating a better understanding of the spatial dynamics of the criminal justice system and informing policy decisions aimed at addressing disparities and promoting equity across different regions of New York State.

## Instructions
1. Clone this repository.
2. Navigate to each directory and run the specified analyses and scripts in the mentioned order to reproduce the analysis.
3. Required libraries: pandas, matplotlib, seaborn.

## Results
The analysis provides insights into the demographic composition, temporal trends, facility distribution, geographical patterns, and crime statistics of incarcerated individuals in NYS for the year 2023.

For any questions or concerns, please contact Hailey Williams (hwilli08@syr.edu).

## Demographics Analysis
- `DEMOGRAPHICS/age_distribution.py`: This script analyzes the age distribution among individuals incarcerated in the snapshot year 2023 and plots a histogram.
- `DEMOGRAPHICS/age_distribution_2023.png`: Histogram visualization of age distribution of incarcerated individuals in NYS in 2023.
- `DEMOGRAPHICS/demographics.py`: This script analyzes demographic statistics (age, gender, race) of incarcerated individuals in NYS for 2023 and presents findings through pie and bar charts.
- `DEMOGRAPHICS/demographics_data.csv`: Dataset containing demographic statistics of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/gender_distribution_pie_chart.png`: Pie chart showing gender distribution of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/race_distribution_bar_chart.png`: Bar chart showing race distribution of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/race_distribution_pie_chart.png`: Pie chart showing race distribution of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/ratios.csv`: Gender and race ratios (Male to Female, Non-white to White) of incarcerated individuals in NYS for 2023.

## Time Series Analysis
- `TIME SERIES/time_series.py`: This script groups the data by year, calculates the count of incarcerated individuals for each year, and creates time series plots showing trends from 2008 to 2023.
- `TIME SERIES/timeseries_race_incarcerated_individuals.png`: Time series plot for trends in incarcerated individuals aggregated by race.
- `TIME SERIES/timeseries_total_incarcerated_individuals.png`: Time series plot for total number of incarcerated individuals.

## Correctional Facility Analysis
- `FACILITY/facility.py`: This script generates stacked bar charts showing racial distribution of incarcerated individuals in NYS in 2023 by correctional facility.
- `FACILITY/top_10_facilities_race_distribution.png`: Stacked bar chart displaying racial distribution for the correctional facilities in NYS with the highest amounts of incarcerated individuals.
- `FACILITY/bottom_10_facilities_race_distribution.png`: Stacked bar chart displaying racial distribution for the correctional facilities in NYS with the lowest amounts of incarcerated individuals.
- `FACILITY/nonwhite_facility_counts.csv`: Counts of non-white individuals in each NYS correctional facility.
- `FACILITY/security_level.py`: This script analyzes trends in incarceration security levels over time in NYS and visualizes the distribution across different security levels.

## Indicting County Analysis
- `INDCOUNTY/indicting_county.py`: This script generates stacked bar charts showing racial distribution of incarcerated individuals in NYS in 2023 by indicting county.
- `INDCOUNTY/top_10_counties_race_distribution.png`: Stacked bar chart displaying racial distribution for the indicting counties in NYS with the highest amounts of incarcerated individuals.
- `INDCOUNTY/bottom_5_counties_race_distribution.png`: Stacked bar chart displaying racial distribution for the indicting counties in NYS with the lowest amounts of incarcerated individuals.
- `INDCOUNTY/nonwhite_county_counts.csv`: Counts of non-white individuals incarcerated in each indicting county.

## Variation in Nonwhite Incarceration
- `VARIATION/nonwhite_variation.py`: This script generates variation plots showing the difference from the average percentage of non-white individuals in 2023 by county of indictment and correctional facility.
- `VARIATION/variation_nonwhite_by_county.png`: Variation plot by indicting county.
- `VARIATION/variation_nonwhite_by_facility.png`: Variation plot by correctional facility.

## Incarceration Choropleth NYS
- `CHOROPLETH/nonwhite_choropleth.py`: This script generates a chloropleth map of the percent nonwhite incarcerated individuals by indicting county in NYS in 2023.
- `CHOROPLETH/nonwhite_choropleth.png`: Chloropleth map.
- `CHOROPLETH/percent_nonwhite_sorted_counties.csv`: Percentage of non-white incarcerated individuals sorted by indicting county.

## Crime Analysis
- `CRIMES/basic_crimes.py`: This script analyzes data for 2023, identifies and visualizes the top 10 most frequent serious crimes committed.
- `CRIMES/top_mostseriouscrimes.png`: Visualization of the most frequent serious crimes.
- `CRIMES/total_crime_counts.csv`: Total counts of each crime.

## Extended Crime Analysis
- `CRIME VS/crimes_heatmap.py`: This script nalyzes the relationship between the top 10 crimes and both the top 25 housing facilities and race/ethnicity of incarcerated individuals in 2023, visualizing the data using heatmaps.
- `CRIME VS/crime_race_heatmap_top10.png`: Heatmap for crime vs. race.
- `CRIME VS/crime_facility_heatmap_top10.png`: Heatmap for crime vs. facility.


