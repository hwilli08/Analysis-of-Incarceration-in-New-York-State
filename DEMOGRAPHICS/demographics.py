import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset for incarcerated individuals under custody
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

# Trimming down to year 2023
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

# Grouping by indicting county and calculating demographic statistics
# Current Age
age_demographics = incarcerated_data_2023.groupby('County of Indictment')['Current Age'].describe()
age_demographics = age_demographics[['mean', '50%', 'min', 'max']]  # Selecting mean, median (50%), min, and max
age_demographics = age_demographics.rename(columns={'mean': 'Mean', '50%': 'Median', 'min': 'Min', 'max': 'Max'})

# Gender
gender_demographics = incarcerated_data_2023.groupby('County of Indictment')['Gender'].value_counts().unstack(fill_value=0)
gender_counts = incarcerated_data_2023['Gender'].value_counts()
male_ratio = gender_counts['MALE'] / gender_counts.sum()
female_ratio = gender_counts['FEMALE'] / gender_counts.sum()

# Race
race_demographics = incarcerated_data_2023.groupby('County of Indictment')['Race/Ethnicity'].value_counts().unstack(fill_value=0)
race_counts = incarcerated_data_2023['Race/Ethnicity'].value_counts()
non_white_count = race_counts.drop('WHITE').sum()
white_count = race_counts['WHITE']
non_white_ratio = non_white_count / race_counts.sum()
white_ratio = white_count / race_counts.sum()

# Saving demographic statistics to CSV file
gender_race_ratios = pd.DataFrame({
    'Gender Ratio (Male to Female)': [male_ratio / female_ratio],
    'Race Ratio (Non-white to White)': [non_white_ratio / white_ratio]
})
demographics_data = pd.concat([age_demographics, gender_demographics, race_demographics], axis=1)
demographics_data.index.name = 'County of Indictment'
demographics_data.columns = ['Mean Age', 'Median Age', 'Min Age', 'Max Age', 'Female', 'Male', 'Asian', 'Non-Hispanic Black', 'Hispanic', 'Native American', 'Non-Hispanic White', 'Other']
demographics_data.to_csv('demographics_data.csv')

# Save ratios to a CSV file with a heading
gender_race_ratios.to_csv('ratios.csv', header=True, index=False)

# Plotting pie and bar charts for gender and race distributions.
# Gender distribution pie chart
plt.figure(figsize=(7, 7))
gender_counts = incarcerated_data_2023['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightcoral'])
plt.title('Gender Distribution of Incarcerated Individuals in New York State (2023)')
plt.tight_layout()
plt.savefig('gender_distribution_pie_chart.png')
plt.show()

# Race distribution bar chart.
plt.figure(figsize=(10, 7))
race_counts = incarcerated_data_2023['Race/Ethnicity'].value_counts()
bars = plt.bar(race_counts.index, race_counts.values, color=['#1f77b4', 'brown', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
plt.xlabel('Race/Ethnicity', fontsize=12)
plt.ylabel('Number of Incarcerated Individuals', fontsize=12)
plt.title('Race/Ethnicity Distribution of Incarcerated Individuals in New York State (2023)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
# Adding data labels above the bars.
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('race_distribution_bar_chart.png')
plt.show()

# Calculate the percentages
non_white_percentage = non_white_count / race_counts.sum() * 100
white_percentage = white_count / race_counts.sum() * 100

# Plotting pie chart for race distribution
plt.figure(figsize=(7, 7))
plt.pie([non_white_percentage, white_percentage], labels=['Non-White', 'White'], autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'skyblue'])
plt.title('Race Distribution of Incarcerated Individuals in New York State (2023)')
plt.tight_layout()
plt.savefig('race_distribution_pie_chart.png')
plt.show()
