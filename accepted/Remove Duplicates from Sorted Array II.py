# coding=utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        left, right, idx = 0, 0, 0
        if size:
            cur = nums[0]
        while right < size:
            right=left
            while right < size and nums[right] == cur:
                right += 1
            if right >= left+2:
                nums[idx], nums[idx+1] = cur , cur
                idx += 2
            elif right == left+1:
                nums[idx] = cur
                idx += 1
            if right < size:
                cur = nums[right]
                left = right
        return idx
