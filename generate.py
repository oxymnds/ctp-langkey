import pandas as pd
import json

# Function to convert a string to snake case
def to_snake_case(s):
    return s.lower().replace(' ', '_')

# Load the CSV file
df = pd.read_csv('output/data.csv')

# Convert the 'Flow' column to snake case
df['Flow'] = df['Flow'].apply(to_snake_case)

# Create the localization keys
df['Localization Key'] = df['Flow'] + '.' + df['Element'] + '.' + df['Context']

# Create the English and Thai dictionaries
en_dict = dict(zip(df['Localization Key'], df['English']))
th_dict = dict(zip(df['Localization Key'], df['Thai']))

# Save the dictionaries to JSON files
with open('output/en.json', 'w') as f:
    json.dump(en_dict, f, ensure_ascii=False, indent=4)

with open('output/th.json', 'w') as f:
    json.dump(th_dict, f, ensure_ascii=False, indent=4)
