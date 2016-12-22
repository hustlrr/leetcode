# coding=utf-8
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) <= 3:
            return False
        for idx in range(3, len(x)):
            if x[idx] >= x[idx - 2] and x[idx - 1] <= x[idx - 3]:
                return True
            if idx >= 4 and x[idx - 1] == x[idx - 3] and x[idx] >= x[idx - 2] - x[idx - 4]:
                return True
            if idx >= 5 and x[idx - 2] >= x[idx - 4] and x[idx - 3] >= x[idx - 1] and x[idx - 1] >= x[idx - 3] - x[
                        idx - 5] and x[idx] >= x[idx - 2] - x[idx - 4]:
                return True
        return False

