# For each index i in array we swap elements up to index 0 in a loop if the elems are not sorted.

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr_idx = i
        while curr_idx > 0 and arr[curr_idx-1] > arr[curr_idx]:
            # swapping
            arr[curr_idx], arr[curr_idx-1] = arr[curr_idx-1], arr[curr_idx]
            curr_idx -= 1
    return arr


# print(insertion_sort([2, 4, 6, 8, 4, 2, 9, 5, 32, 5, 76]))
