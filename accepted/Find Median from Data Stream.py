# coding=utf-8
from heapq import *


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = [] # 小于中位数的堆
        self.large = [] # 大于中位数的堆

    def addNum(self, num):
        """
        Adds a num into the data structure .
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self .large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self .large):
            return (self.large[0] - self .small[0]) * 0.5
        else:
            return self.large[0]

# Your MedianFinder object will be 
