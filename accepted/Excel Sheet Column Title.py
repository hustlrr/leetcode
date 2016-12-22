# coding=utf-8
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        mask=[chr(i+ord('A')) for i in range (26)]
        res=''
        while n:
            res=mask[(n-1)%26]+res
            n=(n-1)/26
        return res
