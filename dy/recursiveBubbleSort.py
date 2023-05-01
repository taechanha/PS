# 1


def bubble_sort(i, arr):
    if i == n:
        return
    if arr[i-1] > arr[i]:
        # swap
        arr[i-1], arr[i] = arr[i], arr[i-1]
    bubble_sort(i+1, arr)


def bubble_sort2(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubble_sort2(arr, n-1)


arr = [9, 6, 2, 12, 11, 9, 3, 7]
n = len(arr)
for i in range(n):
    bubble_sort(1, arr)
    n -= 1
print(arr)

# 2

arr = [9, 6, 2, 12, 11, 9, 3, 7]
n = len(arr)
bubble_sort2(arr, n)
print(arr)
