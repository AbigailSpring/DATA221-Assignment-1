# 1. Store the threshold value in a variable
threshold_value = 100
# Initialize variables(product and multiplier)
product_value = 1
current_multiplier_value = 1
# 2. Keep track of the current multiplier and calculate the product
# The loop will continue as long as the product is not greater than the threshold value
while product_value <= threshold_value:
    current_multiplier_value += 1
    product_value *= current_multiplier_value
# 3. Print the final product and the integer that caused the exeedance
print(f"The threshold value is {threshold_value}.")
print(f"The final product is {product_value}.")
print(f"The integer that caused the product to exceed the threshold was the {current_multiplier_value}.")