# coding=utf-8
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(n): 
            for left in range(1,n - i + 1):
                right = left + i 
                for k in range(left, right + 1):
                    dp[left][right] = max (dp[left][right],\
                                                                 dp[left][k-1] + dp[k +1][right] + nums[k] *nums[left - 1] *nums[right + 1])
        return dp[1][n]
