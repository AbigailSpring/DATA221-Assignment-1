from random import random

random_values_list = [random() for i in range(20)]
threshold_value = random()
random_values_list.sort()
indices_meeting_threshold = []
for idx, value in enumerate(random_values_list):
    if value >= threshold_value:
        indices_meeting_threshold.append(idx)
print("Sorted Random Values:", random_values_list)
print("Threshold Value:", threshold_value)
if indices_meeting_threshold:
    print("First index meeting or exceeding threshold:", indices_meeting_threshold[0])
else:
    print("No values meet or exceed the threshold.")