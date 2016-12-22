# coding=utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        for idx in range(1,len(nums)):
            res=res^nums[idx]
        return res
