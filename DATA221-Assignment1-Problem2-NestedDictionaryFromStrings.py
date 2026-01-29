# 1. Create a function to analyze a list of strings and returns a dictionary with length and parity information
def analyze_length_and_parity_of_the_string(string_list):
    string_details = {}
# 2. Create a for loop to determine the length by using the len() function and determine the parity using the modulo operator
    for current_string in string_list:
        string_length = len(current_string)
        string_parity = "even" if string_length % 2 == 0 else "odd"
        string_details[current_string] = {
            "length": string_length,
            "parity": string_parity
        }
    return string_details
# 3. Test the code by using the words "Data" and "Science"
expected_output_words = ["Data", "Science"]
print(analyze_length_and_parity_of_the_string(expected_output_words))