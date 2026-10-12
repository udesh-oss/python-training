# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break

# data = [73, 28, 49, 26, 42]
# bubble_sort(data)
# print("SORTED DATA = ", data)

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         mini = i
#         for j in range(i+1, n):
#             if arr[j] < arr[mini]:
#                 mini = j
#             arr[i], arr[mini] = arr[mini], arr[i]
# data = [34, 54, 24, 67, 20]
# selection_sort(data)
# print("Selection sort = ", data)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
# data = [34,42,76,33,12]
# bubble_sort(data)
# print("Bubble sort = ", data)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
                arr[i], arr[mini] = arr[mini], arr[i]
data = [24,26,87,46,97,12,9]
selection_sort(data)
print("Selection sort = ", data)