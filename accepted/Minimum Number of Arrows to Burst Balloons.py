# coding=utf-8
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        len_ = len(points)
        num_arrow = 0
        if len_:
            num_arrow = 1
        else:
            return num_arrow
        points = sorted(points, key=lambda _ :_[0]) # 按照起始坐标对区间进行排序
        interval = points[0]
        for point in points:
            start_interval, end_interval = interval
            if point[0] > end_interval:
                interval = point
                num_arrow += 1
            else:
                interval[0] = max (start_interval, point[0])
                interval[1] = min (end_interval, point[1])
        return num_arrow
