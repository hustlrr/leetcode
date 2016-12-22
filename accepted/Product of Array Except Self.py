# coding=utf-8
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #res[i]=nums[0]……nums[i-1]*nums[i +1]……nums[n-1]
        res=[1]
        for i in range(len(nums)-1):
            res.append(res[-1]*nums[i])
        right=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        return res
