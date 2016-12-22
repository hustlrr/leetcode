# coding=utf-8
from collections import OrderedDict


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 1 or not nums:
            return False
        windows = OrderedDict()
        for idx, num in enumerate(nums):
            tmp = num / max(1, t)
            for key in (tmp - 1, tmp, tmp + 1):
                if windows.has_key(key) and abs(num - windows[key]) <= t:
                    return True
            windows[tmp] = num
            if idx >= k:
                windows.popitem(last=False)
        return False
