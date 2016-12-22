# coding=utf-8
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums) - 1
        right, left, cur = size, size / 2, 0
        tmp = sorted(nums)
        while left >= 0 and right > size/2:
            nums[cur] = tmp[left]
            left, cur = left - 1, cur + 1
            nums[cur] = tmp[right]
            right, cur = right - 1, cur + 1
        if left == 0:
            nums[cur] = tmp[left]
