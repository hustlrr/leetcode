# coding=utf-8
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # m个0，n个1
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for s in strs:
            num_zero, num_one = s.count('0' ), s.count('1')
            for i in range(n, num_one - 1, -1):
                for j in range(m, num_zero - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - num_one][j - num_zero] + 1)
        return dp[n][m]
