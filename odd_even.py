numbers = [1,2,3,4,5,6]

grouped_numbers = {
    "even": [num for num in numbers if num % 2 == 0],
    "odd" : [num for num in numbers if num % 2 != 0]
}

print(grouped_numbers)