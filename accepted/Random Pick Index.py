# coding=utf-8
import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        candidates = []
        for idx, num in enumerate(self .nums):
            if num == target:
                candidates.append(idx)
        return random.choice(candidates)

        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)

