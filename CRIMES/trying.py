import pandas as pd

# Read the dataset for incarcerated individuals under custody
incarcerated_data = pd.read_csv("Incarcerated_Individuals_Under_Custody_Beginning_2008.csv")

# Trim down to year 2023
incarcerated_data_2023 = incarcerated_data[incarcerated_data['Snapshot Year'] == 2023]

# Count the number of incarcerated individuals by most serious crime
crime_counts = incarcerated_data_2023['Most Serious Crime'].value_counts().reset_index()
crime_counts.columns = ['Most Serious Crime Committed by Incarcerated Individual', 'Count']

# Read the file into a dataframe
df = pd.read_csv("test-pr1.csv")

# Rename the "gpt" column to "class"
df.rename(columns={"gpt": "class"}, inplace=True)

# Check the length of the string in the class column
is_long = df['class'].str.len() > 30
df.loc[is_long, 'class'] = "other"

# Convert the column to lower case
df['class'] = df['class'].str.lower()



