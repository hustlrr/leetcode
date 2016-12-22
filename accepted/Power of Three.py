# coding=utf-8
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxPowerOfThree=1162261467
        return n>0 and maxPowerOfThree%n==0
