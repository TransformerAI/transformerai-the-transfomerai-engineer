from typing import List

from utils_code.test import assertEq

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    """
    Design a data structure that follows the constraints of a 
    Least Recently Used (LRU) cache.

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        int get(int key) 
            Return the value of the key if the key exists, otherwise return -1.
        void put(int key, int value) 
            Update the value of the key if the key exists. Otherwise, add the 
            key-value pair to the cache. If the number of keys exceeds the capacity 
            from this operation, evict the least recently used key.
    
    The functions get and put must each run in O(1) average time complexity.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0) 
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        

if __name__ == "__main__":
    sol = Solution()
    
    
