# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        for i in range(len(prices)-1):
            prices[i]=prices[i+1]-prices[i]
        res=sum([p for p in prices[:-1] if p >0])
        return res
