# coding=utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,0
        length=len(nums)
        while right<length:
            nums[left]=nums[right]
            while right<length and nums[left]==nums[right]:
                right+=1
            left+=1
        return left
