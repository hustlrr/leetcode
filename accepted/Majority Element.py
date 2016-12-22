# coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numnow=nums[0]
        cntnow=1
        for idx,num in enumerate(nums,1):
            if num!=numnow:
                cntnow-=1
            else:
                cntnow+=1
            if cntnow==0:
                numnow=num
                cntnow=1
        return numnow
