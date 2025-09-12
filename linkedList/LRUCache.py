from sqlalchemy import lateral
from sqlalchemy.dialects.mysql import insert


class DoubleNode:

    def __init__(self, key: int = 0, val: int = 0,  next: 'DoubleNode' = None, prev: 'DoubleNode' = None ):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.cache = {}
        self.oldest = DoubleNode()
        self.latest = DoubleNode()
        self.oldest.next = self.latest
        self.latest.prev = self.oldest


    def get(self, key: int):
        if key in self.cache:
            self.reorder_usage_list(key)
            return self.cache[key].val
        return -1


    def reorder_usage_list(self, key: int):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.latest
        self.latest.prev.next = node
        self.latest.prev = node

    def evict(self, key: int):
        self.oldest.next = self.oldest.next.next
        self.oldest.next.next.prev = self.oldest
        del self.cache[key]

    def insert(self, key, value):
        node = DoubleNode(key, value)
        self.latest.prev.next = node
        node.prev = self.latest.prev
        node.next = self.latest
        self.latest.prev = node
        self.cache[key] = node

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache[key].val = value
            self.reorder_usage_list(key)
        else:
          if self.capacity == len(self.cache):
             self.evict(key)
          self.insert(key, value)
