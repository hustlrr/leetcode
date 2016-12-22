# coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums = sorted(nums, cmp=lambda x, y: -1 if x + y > y + x else 1)
        res = ''.join(nums).lstrip('0')
        return res if res else '0'

