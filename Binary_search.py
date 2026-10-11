def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

    #Check if target is at mid
        if arr[mid] == target:
            return mid
    # If target is greater ignore left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#Search for the number 11
target_value = 11
result = binary_search(sorted_numbers, target_value)
if result != -1:
    print(f"Element {target_value} is found at index {result}")
else:
    print(f"Element {target_value} is not found in list")