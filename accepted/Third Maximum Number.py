# coding=utf-8
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 最初想法是先去重再用快排，后来想了 想直接记录下前三就可以了
        first, second, third = None, None, None
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if first is None:
                first = num
            elif num > first:
                third = second
                second = first
                first = num
            elif second is None:
                second = num
            elif num > second:
                third = second
                second = num
            elif third is None:
                third = num
            elif num > third:
                third = num
        return third if third is not None else first

