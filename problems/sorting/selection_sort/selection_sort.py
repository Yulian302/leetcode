# For each index i in array we find the minimum element starting from [i+1...n-1] and swap it with ith elem.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swapping
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# print(selection_sort([42, 5, 3, 5, 1, 54]))
