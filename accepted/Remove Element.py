# coding=utf-8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx=0
        for n in nums:
            if n!=val:
                nums[idx]=n
                idx+=1
        return idx
