# coding=utf-8
from collections import defaultdict
import random


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = defaultdict(set)
        self.data = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        s = self.index.get(val, None)
        self.index[val].add(len(self.data))
        self.data.append(val)
        if s:
            return False
        else:
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        lastnum = self.data.pop()
        self.index[lastnum].remove(len(self .data))
        if lastnum != val:
            idx = self.index[val].pop()
            self.data[idx] = lastnum
            self.index[lastnum].add(idx)
        if not self.index[val]: # 如果这个元素已经不存在，删除集合 ，否则插入的时候返回值会有错
            del self.index[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.data)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
