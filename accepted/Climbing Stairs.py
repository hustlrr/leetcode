# coding=utf-8
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp=[1,2,3]
        for i in range(3,n):
            tmp[i%3]=tmp[i%3-1]+tmp[i%3-2]
        return tmp[(n-1)%3]

