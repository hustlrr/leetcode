# coding=utf-8
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        dp = [1] * size
        preidx = [-1] * size
        nums = sorted(nums)
        maxsize,maxidx = 0, -1 
        for i in range(size):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    preidx[i] = j
            if dp[i] > maxsize:
                maxsize = dp[i]
                maxidx = i 
        res = []
        while maxidx != -1:
            res.append(nums[maxidx])
            maxidx = preidx[maxidx]
        return res
