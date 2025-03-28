# https://leetcode.com/problems/wiggle-sort/
# Difficulty: Medium
# Tags: sort wiggle_sort

# Problem
# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# You may assume the input array always has a valid answer.

# Solution

from typing import List

# We can use merge sort as a main efficient sorting algorithm. After sorting, we just swap elements every two indices. For example: 1 5 6 3 4 1 6 -> 1 1 3 4 5 6 6 [sorted] -> 1 3 1 5 4 6 6
# either Merge-sort ( O(NlogN) and O(1) )


class Solution:
    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    def merge(self, nums, left, mid, right):
        nLeft = mid - left + 1
        nRight = right - mid
        L = [0] * nLeft
        R = [0] * nRight

        for i in range(nLeft):
            L[i] = nums[left + i]
        for j in range(nRight):
            R[j] = nums[mid + j + 1]

        k = left
        i = j = 0
        while i < nLeft and j < nRight:
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < nLeft:
            nums[k] = L[i]
            i += 1
            k += 1
        while j < nRight:
            nums[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort array
        self.merge_sort(nums, 0, len(nums) - 1)

        for i in range(1, len(nums) - 1, 2):
            self.swap(nums, i, i + 1)


# or simply swap elements at:
# even index if next element is more than curr
# odd index if next element is less than curr

# Time and space ( O(N) and O(1) )

def wiggleSort(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums) - 1):
        if (i & 1 == 0 and nums[i] > nums[i + 1]) or (
            i & 1 == 1 and nums[i] < nums[i + 1]
        ):
            self.swap(nums, i, i + 1)
