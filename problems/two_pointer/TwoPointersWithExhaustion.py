
# Problem
# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

# Solution
# Time O(n+m) and space O(n+m)
# We use two pointers technique. Each pointer is initialized at the beginning of a corresponding array. First we move through the arrays till the end of one of them, appending to our resulting array elements in an increasing order. Then we exhaust an array which is still left. Here we have two posibilities: 1) Arrays are of same length -> no exhaustion will be executed. 2) Arrays are of different lenght -> only one, which is longer will be exhausted.
def combine_two_sorted(arr1, arr2):
    i = j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    # exhaust
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res


print(combine_two_sorted([1, 2, 3], [3, 4, 5, 6, 7]))
