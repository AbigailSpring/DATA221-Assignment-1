threshold_value = 100
product_value = 1
current_multiplier_value = 1
while product_value <= threshold_value:
    current_multiplier_value += 1
    product_value *= current_multiplier_value
print(f"The threshold value is {threshold_value}.")
print(f"The final product is {product_value}.")
print(f"The integer that caused the product to exceed the threshold was the {current_multiplier_value}.")