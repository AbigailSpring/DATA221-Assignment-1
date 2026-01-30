def compute_base_raised_to_exponent(base_value, exponent_value):
    return base_value ** exponent_value
base_exponent_pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
non_negative_exponent_results = []
for base_value, exponent_value in base_exponent_pairs:
    if exponent_value < 0:
        continue
    power_result = compute_base_raised_to_exponent(base_value, exponent_value)
    non_negative_exponent_results.append(power_result)
print(non_negative_exponent_results)