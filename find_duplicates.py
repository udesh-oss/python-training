def find_duplicates(text):
    char_count = {}
    duplicates = []

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    return duplicates

input_string = "hello google"
print("Duplicate characters:", find_duplicates(input_string))
