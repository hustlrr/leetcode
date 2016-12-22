# coding=utf-8
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        freq = collections.Counter(nums1)
        res = []
        for num in nums2:
            if freq[num] > 0:
                freq[num] -= 1
                res.append(num)
        return res
