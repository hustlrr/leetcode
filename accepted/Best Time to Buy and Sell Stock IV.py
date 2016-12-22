# coding=utf-8
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k < len(prices):
            local_ = [0] * (k + 1)
            global_ = [0] * (k + 1)
            for i in range(len(prices) - 1 ):
                diff = prices[i + 1] - prices[i]
                for j in range(k, 0, -1):
                    local_[j] = max (global_[j - 1] + max (diff, 0), local_[j] + diff)
                    global_[j] = max (local_[j], global_[j])
            return global_[k]
        else: # 当k大于交易天数的话，问题等价 于交易次数不限
            res = 0
            for i in range(len(prices) - 1 ):
                diff = prices[i + 1] - 
