def percentage_less_than_or_equal(numbers):
    total_count = len(numbers)
    result = {}
    for value in sorted(set(numbers)):
        count_less_equal = 0
        for num in numbers:
            if num <= value:
                count_less_equal += 1
        result[value] = (count_less_equal/total_count)*100
    return result
numbers = [3, 1, 2, 3, 4, 2]
print(percentage_less_than_or_equal(numbers))