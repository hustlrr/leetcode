# coding=utf-8
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3: return False
        dp=[nums[0]]
        for num in nums[1:]:
            low=0
            high=len(dp)-1
            while low<=high:
                mid=low+(high-low)/2
                if num>dp[mid]:
                    low=mid+1
                else:
                    high=mid-1
            if low>=len(dp):
                dp.append(num)
                if len(dp)==3:
                    return True
            else:
                dp[low]=num
        return False
