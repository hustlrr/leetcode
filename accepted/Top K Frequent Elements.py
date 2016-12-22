# coding=utf-8
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_freq = collections.Counter(nums)
        num_freq_sorted = sorted(num_freq .iteritems(),key = lambda x:x[1] ,reverse = True)
        res = [num_freq_sorted[i][0] for i in range(k)]
        return res
