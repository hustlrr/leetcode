# coding=utf-8
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = low + (high - low) / 2
            if self.canSplitBym(nums, m, mid ):
                # 说明mid可以减小
                high = mid - 1
            else:
                low = mid + 1
        return low

    def canSplitBym(self, nums, m, maxsum):
        cnt = 1
        s = 0
        for num in nums:
            s += num
            if s > maxsum:
                s = num
                cnt += 1
            if cnt > m:
                return False
        return True

