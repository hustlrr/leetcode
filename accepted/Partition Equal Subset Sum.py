# coding=utf-8
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None:
            return True
        s = sum(nums) # 数组的和，如果数组可以分开两部 分，那么每部分一定等于和的一半
        if s % 2: # 如果是和是奇数，一定无法分成两 部分
            return False
        s /= 2
        dp = [False for _ in range(s+1)] # dp[i]表示是否存在一个子集的和等 于i
        dp[0] = True
        for num in nums:
            for i in range(s, num-1, -1): # 应该从大到小，不然相当于一 个数被多次使用了

