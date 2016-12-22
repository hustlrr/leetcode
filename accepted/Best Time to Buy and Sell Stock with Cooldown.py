# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        buys=[-prices[0]]
        sells=[0]
        for i in range(1,len(prices)):
            #第i天卖出的最大收益为第i -1天买入，或第i -1天卖出但后悔
            sells.append(max(buys[i-1] ,sells[i-1]-prices[i-1] )+prices[i])
            if i==1:
                buys.append(buys[i-1] +prices[i-1]-prices[i] )
            else:
            #第i天买入的最大收益为第i -2天卖出，i-1天不运作,或i -1天买入但后悔
                buys.append(max(sells[i-2] ,buys[i-1]+prices[i-1]
