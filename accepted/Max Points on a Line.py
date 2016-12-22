# coding=utf-8
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        for idx1, p1 in enumerate(points):
            gradientsCnt = {} # 不放在外层是因为，只有有一 个共同点且斜率相同时才在一 条直线上，仅通过斜率无法确 定在一条直线上
            same = 0
            for p2 in points[idx1 + 1:]:
                if self.isSamePoints(p1, p2):
                    same += 1
                else:
                    g = self.getGradient (p1, p2)
                    try:
                        gradientsCnt[g] += 1
                    except KeyError:
                        gradientsCnt[g] = 1
            if len(gradientsCnt):
                res = max(res, max (gradientsCnt.values ()) + 1 + same)
            else:
                res = max(res, same + 1)
        return res

    def getGradient(self, p1, p2):
        if p1.x == p2.x:
            return None
        return 1.0 * (p1.y - p2.y) / (p1.x - p2.x)


