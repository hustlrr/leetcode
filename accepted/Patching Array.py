# coding=utf-8
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        cnt = 0
        miss = 1
        idx = 0
        length = len(nums)
        while miss <= n:
            if idx < length and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            else:
                cnt += 1
                miss += miss
        return cnt
