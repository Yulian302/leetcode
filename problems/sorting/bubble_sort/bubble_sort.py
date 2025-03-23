

def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # swapping
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr


print(bubble_sort([3, 4, 67, 4, 432, 3]))
