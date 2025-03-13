# https://leetcode.com/problems/sort-list
# Difficulty: Medium
# Tags: sorting merge_sort linked_list

# Problem
# Given the head of a linked list, return the list after sorting it in ascending order.

# Solution
# Time O(NlogN) and space O(N)
# Divide and conquer method! We recursively (using dfs) divide our array into half until we get one element left. Then comes the next recursive function call that processes another half. Finally we call the last function on both halves to merge them into a sorted array. It all can be visualized using a tree data structure. But the main difference is that we do that for a linked list data structure. So we work with pointers, we use dummy node etc.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMid(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return prev

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None
        left_half = self.sortList(left)
        right_half = self.sortList(right)

        return self.merge(left_half, right_half)
