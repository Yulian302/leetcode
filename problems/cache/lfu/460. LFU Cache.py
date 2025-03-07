# https://leetcode.com/problems/lfu-cache/
# Difficulty: Hard
# Tags: cache lfu doubly_linked_list hash_map frequency

# Problem
# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

#     LFUCache(int capacity) Initializes the object with the capacity of the data structure.
#     int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
#     void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.


# Solution
# Time O(1) and space O(1) for get and put methods.
# In order to implement a LFU (least frequently used) cache and reach constant time for: 1)Getting a value from cache using a key. 2)Updating a cache value. , we need to build some logic on top of existing LRU cache solution. It is crucial, because if the freq for both elements are same, cache must evict least recently used element. So, in simple words, LFU can be implemented using a hash map with keys as frequencies and values as existing doubly linked lists (cache elements). Then when we do a cache hit, the freq table is updated and the node is moved to the corresponding freq to the beginning of a DDL. Thus, we can still evict a LRU item when LFU is ambiguous due to duplicate frequencies.


from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_tail(self):
        if self.size > 0:
            lru_node = self.tail.prev
            self.remove(lru_node)
            return lru_node
        return None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.freq_map = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def _update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0 and self.min_freq == freq:
            self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].insert_front(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update_freq(node)
        else:
            if len(self.node_map) >= self.capacity:
                lfu_node = self.freq_map[self.min_freq].pop_tail()
                del self.node_map[lfu_node.key]

            node = Node(key, value)
            self.node_map[key] = node
            self.freq_map[1].insert_front(node)
            self.min_freq = 1
