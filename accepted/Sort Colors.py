# coding=utf-8
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt=[0,0,0]
        for num in nums:
            cnt[num]+=1
        for i in range(cnt[0]):
            nums[i]=0
        for i in range(cnt[0],cnt[0]+cnt[1] ):
            nums[i]=1
        for i in range(cnt[0]+cnt[1],cnt[0] +cnt[1]+cnt[2]):
            nums[i]=2
