# coding=utf-8
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor=5
        cnt=0
        while factor<=n:
            cnt+=n/factor
            factor*=5 
        return cnt
