import pandas as pd

# --- Part 1: Series of calories ---
calories = {
    "Day 01": 1750,
    "Day 02": 2100,
    "Day 03": 1700
}

series = pd.Series(calories)

# Filter days with calories >= 2000
high_calories = series[series >= 2000]
print("Days with calories >= 2000:")
print(high_calories)
print("\n")

# --- Part 2: DataFrame of people ---
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data)

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

print("Original DataFrame:")
print(df)
print("\n")

# --- Part 3: Add a new row ---
# Using pd.DataFrame + pd.concat
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}], index=["04"])
df = pd.concat([df, new_row])

print("DataFrame after adding new row:")
print(df)

