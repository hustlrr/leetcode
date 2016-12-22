# coding=utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numlen=len(nums)
        nums[0:k],nums[k:numlen]=nums[numlen -k:numlen],nums[0:numlen-k]
