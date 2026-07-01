import pandas as pd

# Read CSV file
df = pd.read_csv("emp.csv")

# Convert to JSON
df.to_json("employees.json", orient="records", indent=4)

print("CSV has been converted to JSON successfully!")