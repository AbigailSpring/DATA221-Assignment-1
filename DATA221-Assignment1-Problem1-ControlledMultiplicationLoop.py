multiplication_threshold_value = 100
factorial_product_until_threshold_value = 1
integer_that_exceeds_threshold_value = 1
while factorial_product_until_threshold_value <= multiplication_threshold_value:
    integer_that_exceeds_threshold_value += 1
    factorial_product_until_threshold_value *= integer_that_exceeds_threshold_value
print(f"The threshold value is {multiplication_threshold_value}.")
print(f"The final product is {factorial_product_until_threshold_value}.")
print(f"The integer that caused the product to exceed the threshold was " f"{integer_that_exceeds_threshold_value}.")