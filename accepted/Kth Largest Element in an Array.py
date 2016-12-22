# coding=utf-8
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums[:k]=sorted(nums[:k],reverse =True)
        for i in range(k,len(nums)):
            for j in range(k):
                if nums[i]>nums[j]:
                    tmp=nums[i]
                    nums[j+1:k+1]=nums[j:k]
                    nums[j]=tmp
                    break
        return nums[k-1]
