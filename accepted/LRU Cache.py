# coding=utf-8
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        value = self.cache.pop(key, default =None)
        if value is None:
            return -1
        self.cache[key] = value
        return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.cache.pop(key, default=None) is None and len(self.cache) == self.capacity:
            self.cache.popitem(last=False) # 先进先出
        self.cache[key] = value

