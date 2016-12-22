# coding=utf-8
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        mask=1
        while n!=0:
            cnt+=(n&mask)
            n>>=1
        return cnt
