# coding=utf-8
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt=0
        while n>=1:
            cnt+=(n&1)
            n>>=1
        return cnt==1
