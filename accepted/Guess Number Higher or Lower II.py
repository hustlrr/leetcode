# coding=utf-8
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for r in range(1, n):
            for left in range(1, n - r + 1):
                right = left + r
                dp[left][right] = min([x + max(dp[left][x - 1], dp[x + 1][right]) for x in range(left, right)])
        return dp[1][n]
