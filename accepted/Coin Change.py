# coding=utf-8
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = 0
        dp = [amount + 1 for i in range (amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i - coin] + 1 , dp[i])
        return dp[amount] if dp[amount] < amount + 1 else -1
