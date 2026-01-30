def build_string_length_and_parity_dictionary(list_of_words):
    string_to_properties_map = {}
    for word in list_of_words:
        length_of_word = len(word)
        parity_of_length = "even" if length_of_word % 2 == 0 else "odd"
        string_to_properties_map[word] = {
            "length": length_of_word,
            "parity": parity_of_length
        }
    return string_to_properties_map
input_words = ["Data", "Science"]
print(build_string_length_and_parity_dictionary(input_words))