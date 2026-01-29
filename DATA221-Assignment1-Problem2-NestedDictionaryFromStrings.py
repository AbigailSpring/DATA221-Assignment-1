def analyze_length_and_parity_of_the_string(string_list):
    string_details = {}
    for current_string in string_list:
        string_length = len(current_string)
        string_parity = "even" if string_length % 2 == 0 else "odd"
        string_details[current_string] = {
            "length": string_length,
            "parity": string_parity
        }
    return string_details
expected_output_words = ["Data", "Science"]
print(analyze_length_and_parity_of_the_string(expected_output_words))