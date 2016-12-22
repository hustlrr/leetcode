# coding=utf-8
import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        #只有i是完全平方数时，第i只灯泡会亮 着
        #小于n的完全平方数的个数为对n开方
        return int(math.sqrt(n))
