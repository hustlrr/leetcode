# coding=utf-8
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def getMaxSubArray(nums, n): # 得到包含n个元素的子数组
            res = []
            size = len(nums)
            for idx, num in enumerate(nums ):
                while res and len(res) + size - idx > n and num > res[-1]:
                    res.pop()
                if len(res) < n:
                    res.append(num)
            return res

        def merge(nums1, nums2): # 合并两个数组
            return [max(nums1, nums2).pop (0) for _ in range(len (nums1) + len(nums2))]

        res = []
        for len1 in range(max(0, k - len (nums2)), min(k, len(nums1)) + 1):
            tmp1 = getMaxSubArray(nums1, len1)
            tmp2 = getMaxSubArray(nums2, k - len1)
            res = max(res, merge(tmp1, 
