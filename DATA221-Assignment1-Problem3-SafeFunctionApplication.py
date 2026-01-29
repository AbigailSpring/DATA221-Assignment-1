# 1. Create a function that computes x^y
def compute_power(base, exponent):
    return base ** exponent
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
power_results = []
# Use the "for" loop to unpack the argument
for base, exponent in pairs:
# The if-statement below skips past negative numbers
    if exponent < 0:
        continue
    power_results.append(compute_power(base, exponent))

print(power_results)