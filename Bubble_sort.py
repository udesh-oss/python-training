def bubble(arr):
    n = len(arr)
#Outer loop to access each array element
    for i in range(n):
        swapped = False
#Inner loop for adjacents comparison
#The last i elements are already in place
        for j in range(0, n - i - 1):
#Swap if the element found is greater than the nex element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

#Example
data = [64, 34, 25, 12, 22, 11, 90]
bubble(data)
print("Sorted Array:", data)