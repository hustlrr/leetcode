# coding=utf-8
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2) 
        len1, len2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        res = []
        while idx1 < len1 and idx2 < len2:
            if nums1[idx1]==nums2[idx2]:
                res.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return list(set(res))
