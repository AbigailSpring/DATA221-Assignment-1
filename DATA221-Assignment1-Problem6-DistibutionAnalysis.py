def calculate_percentage_less_than_or_equal(numbers_in_list):
    total_numbers = len(numbers_in_list)
    percentage_dict = {}
    for unique_value in sorted(set(numbers_in_list)):
        count_less_equal = 0
        for number in numbers_list:
            if number <= unique_value:
                count_less_equal += 1
        percentage_dict[unique_value] = (count_less_equal / total_numbers) * 100
    return percentage_dict
numbers_list = [3, 1, 2, 3, 4, 2]
print(calculate_percentage_less_than_or_equal(numbers_list))