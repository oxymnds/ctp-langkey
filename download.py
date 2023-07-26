import requests
import pandas as pd
from io import StringIO

# Convert the Google Sheets URL to the CSV export URL
google_sheet_id = '1roWpmHviID7D0_D6FgpNeV7DNtxsApogXpTJFvzBV7g'
gid = '1839883585'
csv_export_url = f'https://docs.google.com/spreadsheets/d/{google_sheet_id}/export?format=csv&gid={gid}'

# Make a GET request to the URL
response = requests.get(csv_export_url)

# Ensure the response encoding is correct
response.encoding = 'utf-8'

# Convert the response content to a pandas DataFrame
df = pd.read_csv(StringIO(response.text))

# Remove all rows with missing values
df = df.dropna(how='all')

# Write the DataFrame to a CSV file
df.to_csv('output/data.csv', index=False)
