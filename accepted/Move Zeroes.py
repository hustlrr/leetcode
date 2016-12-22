# coding=utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        px,py=0,0
        for px in range(len(nums)):
            if nums[px]!=0:
                nums[py]=nums[px]
                py+=1
        tmp=py
        for py in range(tmp,len(nums)):
            nums[py]=0
