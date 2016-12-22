# coding=utf-8
from collections import defaultdict


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left, bottom = min(_[0] for _ in rectangles), min(_[1] for _ in rectangles)
        right, top = max(_[2] for _ in rectangles), max(_[3] for _ in rectangles)

        points = defaultdict(int)
        for L, B, R, T in rectangles:
            if points[(L, B)] & 1: # 每个顶点只能是一个方块的左上 角，其他角同理
                return False
            points[(L, B)] |= 1
            if points[(R, B)] & 2:
                return False
            points[(R, B)] |= 2
            if points[(R, T)] & 4:
                return False
            points[(R, T)] |= 4
            if points[(L, T)] & 8:
                return False
            points[(L, T)] |= 8
        for px, py in points: # 保证小方块的集合是一个大方块
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3, 6, 9, 12, 15): # 内部顶点一定要在边界上
                    return False
        return True

