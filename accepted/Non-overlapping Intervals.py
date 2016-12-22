# coding=utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # 按照结束时间从小到大排序
        intervals = sorted(intervals, key =lambda _:_.end)
        num_interval = len(intervals)
        # 计算不重叠的区间的个数
        cnt, end_now = 0, None
        if num_interval:
            cnt = 1
            end_now = intervals[0].end
        else:
            return cnt
        i = 1
        while i < num_interval:
            if intervals[i].start >= end_now:
                cnt += 1
                end_now = intervals[i].end
            i += 1
        return num_interval - cnt # 总区间个数减去最大不重叠区间个
