# coding=utf-8
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=len(nums)*(len(nums)+1)/2
        for num in nums:
            res-=num
        return res
