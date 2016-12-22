# coding=utf-8
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        start, end = 0, len(nums) - 1
        moves = 0
        while start < end:
            moves += (nums[end] - nums[start])
            start += 1
            end -= 1
        return moves
