# https://leetcode.com/problems/sort-an-array/
# Difficulty: Medium
# Tags: sorting merge_sort

# Problem
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Solution
# Time O(NlogN) and space O(N)
# Divide and conquer method! We recursively (using dfs) divide our array into half until we get one element left. Then comes the next recursive function call that processes another half. Finally we call the last function on both halves to merge them into a sorted array. It all can be visualized using a tree data structure.


from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        if len(nums) == 1:
            return [nums[0]]

        def merge(left, mid, right):
            left_part = nums[left: mid + 1]
            right_part = nums[mid + 1: right + 1]
            n = len(left_part)
            m = len(right_part)
            i = j = 0
            k = left  # pointer for resulting arr
            while i < n and j < m:
                if left_part[i] <= right_part[j]:
                    nums[k] = left_part[i]
                    i += 1
                else:
                    nums[k] = right_part[j]
                    j += 1
                k += 1

            # exhaust
            while i < n:
                nums[k] = left_part[i]
                i += 1
                k += 1

            while j < m:
                nums[k] = right_part[j]
                j += 1
                k += 1

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)

            return nums

        return merge_sort(0, len(nums) - 1)
