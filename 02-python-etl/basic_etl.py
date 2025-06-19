import pandas as pd

# Extract
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 32, 30]
}
df = pd.DataFrame(data)

# Transform
df['age_plus_10'] = df['age'] + 10

# Load
df.to_csv('02-python-etl/output.csv', index=False)

print("ETL pipeline complete. Data written to output.csv")
