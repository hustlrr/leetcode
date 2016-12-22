# coding=utf-8
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n-1
        dp=[0,1,2,3]
        for i in range(4,n+1):
            dp.append(max(3*dp[i-3],2*dp[i -2]))
        return dp[n]
