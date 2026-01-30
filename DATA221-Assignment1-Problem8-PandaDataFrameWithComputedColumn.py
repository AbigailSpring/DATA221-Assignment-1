import pandas as pd

data_dict = {
    "category_id": [1, 2, 2, 1],
    "measurement_value": [3.1, 4.2, 1.5, 6.3],
    "quantity": [800, 150, 400, 210]
}

df = pd.DataFrame(data_dict)

df["total_value"] = df["category_id"] * df["quantity"]

print(df)