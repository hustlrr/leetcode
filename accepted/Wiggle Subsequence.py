# coding=utf-8
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag, cnt = 0, 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1] and (flag == 0 or flag == -1):
                flag = 1
                cnt += 1
            elif nums[i] > nums[i - 1] and (flag == 0 or flag == 1):
                flag = -1
                cnt += 1
        return cnt if len(nums) else 0
