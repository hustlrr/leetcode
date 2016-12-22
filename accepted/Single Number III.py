# coding=utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lowbit=0
        for num in nums:
            lowbit=lowbit^num
        lowbit=lowbit&(-lowbit)
        res=[0,0]
        for num in nums:
            if lowbit&num:
                res[0]=res[0]^num
            else:
                res[1]=res[1]^num
        return res
