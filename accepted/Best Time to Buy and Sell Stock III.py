# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 1:
            return 0
        forward = [0 for _ in range(n)]
        backward = [0 for _ in range(n)]

        lowest = prices[0]
        for i in range(1, n):
            lowest = min(lowest, prices[i] )
            forward[i] = max(forward[i - 1], prices[i] - lowest)
        highest = prices[n - 1]
        for i in range(n - 2, -1, -1):
            highest = max(highest, prices[i])
            backward[i] = max(backward[i + 1], highest - prices[i])


