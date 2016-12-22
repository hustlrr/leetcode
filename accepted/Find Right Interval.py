# coding=utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def findRightInterval(self, intervals ):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        idx = {} # key是每个interval的start，valu e是每个interval在intervals数组 中的序号
        for i, interval in enumerate (intervals):
            idx[interval.start] = i

        intervals = sorted(intervals, key =lambda _:_.start)
        len_ = len(intervals)
        res = [-1] * len_
        for interval in intervals:
            start_now = interval.start
            end_now = interval.end # 二分查找
            low, high = 0, len_ - 1
            while low <= high:
                mid = low + (high - low)/2
                if intervals[mid].start == end_now:
                    res[idx[start_now]] = idx[intervals[mid] .start]
                    break
                if intervals[mid].start > end_now:
                    high = mid - 1
                else:
                    low = mid + 1
            if low < len_ and low > high:
                res[idx[start_now]] = idx[intervals[low] .start]

