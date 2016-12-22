# coding=utf-8
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        k = int(math.sqrt(2 * n))
        while k * (k + 1) <= 2 * n:
            k += 1
        return k - 1
