def compute_power(base, exponent):
    return base ** exponent
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
power_results = []
for base, exponent in pairs:
    if exponent < 0:
        continue
    power_results.append(compute_power(base, exponent))

print(power_results)