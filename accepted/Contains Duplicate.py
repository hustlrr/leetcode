# coding=utf-8
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp=set(nums)
        return len(tmp)!=len(nums)
