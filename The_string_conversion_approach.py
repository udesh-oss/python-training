num = 456
digit_sum = sum(int(digit) for digit in str(num))
print(f"The sum of the digits in {num} is: {digit_sum}")

a = 4
b = 16
print(f"Before swap a = {a} and b = {b}")

temp = a
a = b
b = temp
print(f"After swap a = {a} and b = {b}")

a = 5
b = 10
print(f"Before swap a = {a} and b = {b}")

a, b = b, a
print(f"After swap a = {a} and b = {b}")

a = 5
b = 8
c = 10
largest = max(a, b, c)
print(f"The largest number is: {largest}")