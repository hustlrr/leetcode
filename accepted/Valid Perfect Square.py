# coding=utf-8
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i*i < num:
            i += 1
        return i*i == num 
