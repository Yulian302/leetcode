# Naive Heap Sort: we simply heapify our input array, create a new resulting array and populate it one by one popping a minimum from heap.
# Time O(NlogN) and space O(N)

# Optimized Heap Sort: constant space (in-place sorting).
# We have to be familiar with heap implementation details using an array. First we have to max heapify the input array from bottom to top. Thus, we now have a maximum element as root. Then we swap the root element (max) with the last element, making end of array sorted and heapifying again. We repeat this process again and again decreasing the heap size until one element is left.
# Time O(NlogN) and space O(1)

import heapq


def heap_sort_naive(arr):
    res = []
    heapq.heapify(arr)  # O(N)
    for _ in range(len(arr)):  # O(N)
        res.append(heapq.heappop(arr))  # O(logN)
    return res


def heap_sort_optimized(arr):
    n = len(arr)

    def max_heapify(heap_size, index):
        largest = index
        left = 2*index+1
        right = 2*index+2
        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != index:
            # swapping
            arr[largest], arr[index] = arr[index], arr[largest]
            max_heapify(heap_size, largest)

    # initial bottom up max heapify
    for i in range(n//2-1, -1, -1):
        max_heapify(n, i)

    # swapping max and last elem and heapifying
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(i, 0)

    return arr


# print(heap_sort_naive([3, 5, 2, 2, 4, 78, 5, 4, 2]))
# print(heap_sort_optimized([3, 5, 2, 2, 4, 78, 5, 4, 2]))
