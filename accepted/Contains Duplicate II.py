# coding=utf-8
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmp={}
        for idx,num in enumerate(nums):
            try:
                if idx-tmp[num]<=k:
                    return True
                tmp[num]=idx
            except KeyError:
                tmp[num]=idx
        return False
