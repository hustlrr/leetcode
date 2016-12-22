# coding=utf-8
#coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #yes:盗窃了上一家所获得的收益
        #no:未盗窃上一家所获得的收益
        yes,no=0,0
        for profit in nums:
            yes,no=no+profit,max(yes,no)
        return max(yes,no)
