# Analysis of Incarcerated Individuals in New York State

This repository houses a comprehensive analysis of incarcerated individuals' demographics, trends, facilities, and crimes in New York State for the year 2023. It includes scripts written in Python for data processing, visualization, and interpretation. The analysis covers a wide range of aspects, including age, gender, race, time series trends, facility distribution, indicting county demographics, variation from average non-white percentages, choropleth mapping, and crime statistics. Each script is meticulously documented, detailing its purpose and methodology. The provided visualizations offer clear insights into the distribution and characteristics of the incarcerated population, aiding policymakers, researchers, and the public in understanding and addressing issues related to incarceration, demographics, and criminal justice in New York State. 

## Input Data Sources
- [Incarcerated Individuals Under Custody Beginning 2008](https://data.ny.gov/Public-Safety/Incarcerated-Individuals-Under-Custody-Beginning-2/55zc-sp6m/about_data)

This core dataset provides comprehensive information on individuals under custody in New York State, starting from 2008. It encompasses data on demographics, crimes committed, and facility details, offering insights into trends and patterns within the state's criminal justice system over time. 

- [NYS Civil Boundaries](https://data.gis.ny.gov/datasets/sharegisny::nys-civil-boundaries/explore?layer=2&location=42.846702%2C-78.687173%2C7.82&showTable=true)

By providing detailed geographical boundaries of administrative units such as counties, cities, towns, and villages within New York State, this dataset enables the creation of accurate and informative choropleth maps that depict various socio-demographic characteristics, including the distribution of incarcerated individuals by indicting county. Choropleth maps created using this dataset allow for the visualization of regional disparities in incarceration rates, facilitating a better understanding of the spatial dynamics of the criminal justice system and informing policy decisions aimed at promoting equity across different regions of New York State.

## Instructions
Download the required libraries (pandas, matplotlib, and tabulate).

To obtain the original input data used in this analysis, follow these steps:

1. **Incarcerated Individuals Under Custody Beginning 2008:**
   - Visit the [Incarcerated Individuals Under Custody Beginning 2008 dataset](https://data.ny.gov/Public-Safety/Incarcerated-Individuals-Under-Custody-Beginning-2/55zc-sp6m/about_data).
   - Download the dataset from the provided link.

2. **NYS Civil Boundaries:**
   - Access the [NYS Civil Boundaries dataset](https://data.gis.ny.gov/datasets/sharegisny::nys-civil-boundaries/explore?layer=2&location=42.846702%2C-78.687173%2C7.82&showTable=true).
    - Download the dataset from the provided link.

Clone this repository. To reproduce the analysis, follow the order in which the scripts should be run:

1. **Demographics Analysis:**
   - Run `DEMOGRAPHICS/age_distribution.py` to analyze age distribution among incarcerated individuals.
   - Run `DEMOGRAPHICS/demographics.py` to analyze demographic statistics (age, gender, race) and generate visualizations.

2. **Time Series Analysis:**
   - Execute `TIME SERIES/time_series.py` to generate time series plots for trends in the number of incarcerated individuals over the years
  
3. **Correctional Facility Analysis:**
   - Run `FACILITY/facility.py` to analyze racial distribution of incarcerated individuals by correctional facility.
   - Execute `FACILITY/security_level.py` to analyze trends in incarceration security levels over time.

4. **Indicting County Analysis:**
   - Run `INDCOUNTY/indicting_county.py` to analyze racial distribution of incarcerated individuals by indicting county.

5. **Variation in Nonwhite Incarceration:**
   - Execute `VARIATION/nonwhite_variation.py` to generate variation plots showing differences in non-white incarceration percentages.

6. **Incarceration Choropleth NYS:**
   - Run `CHOROPLETH/nonwhite_choropleth.py` to generate a chloropleth map showing the percent of nonwhite incarcerated individuals by indicting county in New York State.

7. **Crime Analysis:**
   - Execute `CRIMES/basic_crimes.py` to analyze the top 10 most frequent serious crimes committed.

8. **Extended Crime Analysis:**
   - Run `CRIME VS/crimes_heatmap.py` to analyze the relationship between top crimes and race/facility using heatmaps.

By following these instructions and running the scripts in the specified order, you can reproduce the analysis conducted in this repository.

## Results
The analysis provides insights into the demographic composition, temporal trends, facility distribution, geographical patterns, and crime statistics of incarcerated individuals in NYS for the year 2023.

For any questions or concerns, please contact Hailey Williams (hwilli08@syr.edu).

## Demographics Analysis Outputs
- `DEMOGRAPHICS/age_distribution_2023.png`: Histogram visualization of age distribution of incarcerated individuals in NYS in 2023.
- `DEMOGRAPHICS/demographics_data.csv`: Dataset containing demographic statistics of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/gender_distribution_pie_chart.png`: Pie chart showing gender distribution of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/race_distribution_bar_chart.png`: Bar chart showing race distribution of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/race_distribution_pie_chart.png`: Pie chart showing race distribution of incarcerated individuals in NYS for 2023.
- `DEMOGRAPHICS/ratios.csv`: Gender and race ratios (Male to Female, Non-white to White) of incarcerated individuals in NYS for 2023.

## Time Series Analysis Outputs
- `TIME SERIES/timeseries_race_incarcerated_individuals.png`: Time series plot for trends in incarcerated individuals aggregated by race.
- `TIME SERIES/timeseries_total_incarcerated_individuals.png`: Time series plot for total number of incarcerated individuals.

## Correctional Facility Analysis Outputs
- `FACILITY/top_10_facilities_race_distribution.png`: Stacked bar chart displaying racial distribution for the correctional facilities in NYS with the highest amounts of incarcerated individuals.
- `FACILITY/bottom_10_facilities_race_distribution.png`: Stacked bar chart displaying racial distribution for the correctional facilities in NYS with the lowest amounts of incarcerated individuals.
- `FACILITY/nonwhite_facility_counts.csv`: Counts of non-white individuals in each NYS correctional facility.
- `FACILITY/security_level_pie.png`:
- `FACILITY/security_level_trends.png`:

## Indicting County Analysis Outputs
- `INDCOUNTY/top_10_counties_race_distribution.png`: Stacked bar chart displaying racial distribution for the indicting counties in NYS with the highest amounts of incarcerated individuals.
- `INDCOUNTY/bottom_5_counties_race_distribution.png`: Stacked bar chart displaying racial distribution for the indicting counties in NYS with the lowest amounts of incarcerated individuals.
- `INDCOUNTY/nonwhite_county_counts.csv`: Counts of non-white individuals incarcerated in each indicting county.

## Variation in Nonwhite Incarceration Outputs
- `VARIATION/variation_nonwhite_by_county.png`: Variation plot by indicting county.
- `VARIATION/variation_nonwhite_by_facility.png`: Variation plot by correctional facility.

## Incarceration Choropleth NYS Output
- `CHOROPLETH/nonwhite_choropleth.png`: Chloropleth map.
- `CHOROPLETH/percent_nonwhite_sorted_counties.csv`: Percentage of non-white incarcerated individuals sorted by indicting county.

## Crime Analysis Outputs
- `CRIMES/top_mostseriouscrimes.png`: Visualization of the most frequent serious crimes.
- `CRIMES/total_crime_counts.csv`: Total counts of each crime.

## Extended Crime Analysis Outputs
- `CRIME VS/crime_race_heatmap_top10.png`: Heatmap for crime vs. race.
- `CRIME VS/crime_facility_heatmap_top10.png`: Heatmap for crime vs. facility.


