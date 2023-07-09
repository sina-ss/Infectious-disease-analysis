import pandas as pd

# Read in the Excel file and create a pandas DataFrame
df = pd.read_excel("test-results.xlsx")

# View the first 5 rows of the DataFrame
print(df.head())