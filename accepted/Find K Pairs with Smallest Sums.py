# coding=utf-8
import heapq
import itertools

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k ):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        return min(list, heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum))
