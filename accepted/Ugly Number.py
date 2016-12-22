# coding=utf-8
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0: return False
        divs=[2,3,5]
        for div in divs:
            while num%div==0:
                num/=div
        return num==1
