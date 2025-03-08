# https://leetcode.com/problems/find-median-from-data-stream/
# Difficulty: Hard
# Tags: data_stream stream median heap min_heap max_heap

# Problem
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

#     For example, for arr = [2,3,4], the median is 3.
#     For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:

#     MedianFinder() initializes the MedianFinder object.
#     void addNum(int num) adds the integer num from the data stream to the data structure.
#     double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


# Solution
# Time O(logn) for addNum and O(1) for findMedian; space O(n)
# We can use min and max heap for this problem. When the new number is added, we push it into max heap, then pop it from max heap and push into min heap. Meanwhile we have to prevent min heap from being bigger that max heap. To find a median, we check if max heap is bigger. if it is the root element is a median, otherwise we add root elements from both heaps and divide by half.

import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
