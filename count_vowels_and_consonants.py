def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonants_counts = 0

    for char in text:
        if char.isalpha:
            if char in vowels:
                vowel_count += 1
            else:
                consonants_counts += 1
    return vowel_count, consonants_counts

sample_text = "Hello World! 2026"
vowel_count, consonants_counts = count_vowels_and_consonants(sample_text)
print(f"Original Text: {sample_text}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonants_counts}")