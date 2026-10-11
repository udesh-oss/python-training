def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num >largest:
            largest = num
    return largest

my_list = [12, 45, 2, 76, 42, 52]
result = find_largest_number(my_list)
print(f"The largest number is:", result)
