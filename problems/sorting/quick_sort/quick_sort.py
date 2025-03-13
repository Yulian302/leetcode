
def swap(arr, i, j):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right):
    pivot = arr[right]
    i = left-1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i+1, right)
    return i+1


def quick_sort(arr, left, right):
    if left >= right:
        return

    partition_idx = partition(arr, left, right)

    quick_sort(arr, left, partition_idx-1)
    quick_sort(arr, partition_idx+1, right)


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)
