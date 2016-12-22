# coding=utf-8
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if num > t:
                    break
                dp[t] += dp[t - num]
        return dp[target]
