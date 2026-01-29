import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add a new column derived from existing columns
# Example: multiply columns A and C
df["D"] = df["A"] * df["C"]

# Print the final DataFrame
print(df)