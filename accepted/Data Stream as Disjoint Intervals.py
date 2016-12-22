# coding=utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        new_intervals = []
        cur = Interval(val, val)
        pos = 0
        for interval in self.intervals:
            if interval.start - 1 > cur .end :#无需合并，且位置在当前位 置之前，所以pos不再改变
                new_intervals.append (interval)
            elif interval.end + 1 < cur .start :#无需合并，但位置在当前位 置之后，所以pos+1
                new_intervals.append (interval)
                pos += 1
            else :#需要合并，所以当前的inte rval暂时不加入，将当前的i nterval和cur合并，并记录下 将要插入的位置pos
                cur.start = min(cur.start, interval.start)
                cur.end = max(cur.end, interval.end)
        new_intervals.insert(pos, cur)
        self.intervals = new_intervals
#         for interval in self.intervals:
#             print '[%d, %d]'%(interval .start, interval.end)
#         print '*'*30

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:

