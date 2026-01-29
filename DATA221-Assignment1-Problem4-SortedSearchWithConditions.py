from random import random
values = [random() for i in range(20)]
x = random()
values.sort()
matching_indices = []
for index, value in enumerate(values):
    if value >= x:
        matching_indices.append(index)
print("Sorted Values:", values)
print("X:", x)
if matching_indices:
    print("First matching index:", matching_indices[0])
else:
    print("No values are greater than or equal to x.")