# coding=utf-8
class Solution(object):
    dp = [0, 1]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        size = len(self.dp)
        while size <= n:
            m = size
            val = n
            i = 1
            while i*i <= m:
                val = min(val, self.dp[m-i *i]+1)
                i += 1
            self.dp.append(val)
            size += 1
        return self.dp[n]
