# coding=utf-8
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ = min(nums) # 提高n -1个元素的值，相当于1个元素减1
        # 所以结果应该等于每个元素减去最小元 素的差的和
        res = 0
        for num in nums:
            res += (num - min_)
        return res
