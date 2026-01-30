import pandas as pd

data_dict = {
    "category_id": [1, 2, 2, 1],
    "measurement_value": [3.1, 4.2, 1.5, 6.3],
    "quantity": [800, 150, 400, 210]
}
modified_data_dict_into_data_frame = pd.DataFrame(data_dict)
modified_data_dict_into_data_frame["total_value"] = modified_data_dict_into_data_frame["category_id"] * modified_data_dict_into_data_frame["quantity"]
print(modified_data_dict_into_data_frame)