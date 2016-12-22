# coding=utf-8
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_num=len(nums)
        dp=[1 for i in range(len_num)]
        for i in range(len_num):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp) if len_num!=0 else 0
