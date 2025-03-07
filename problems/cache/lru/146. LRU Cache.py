# https://leetcode.com/problems/lru-cache/
# Difficulty: Medium
# Tags: cache lru doubly_linked_list hash_map

# Problem
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.


# Solution
# Time O(1) and space O(1) for get and put methods
# In order to implement a LRU (least recently used) cache and reach constant time for: 1)Getting a value from cache using a key. 2)Updating a cache value. , we can use Doubly Linked List along with hash map. In the DDL when we get the value from cache, the corresponding node is removed from list and appended to the beginning. When we update the cached value, we remove it from the cache if it exists and then append to the beginning as well. Thus, least recently used element will always stay at the end of list. So, when cache capacity reaches its maximum, cache evicts the last value in a DDL.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._insert(node)

        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
