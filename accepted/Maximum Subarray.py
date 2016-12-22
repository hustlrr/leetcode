# coding=utf-8
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        maxSum=nums[0]
        included=[nums[0]] #included[i]表示包含nums[i]的最大 子序列和
        for i in range(1,len(nums)):
            if included[-1]<0:
                included.append(nums[i])
            else:
                included.append(nums[i] +included[-1])
            maxSum=max(maxSum,included[-1])
        return maxSum
