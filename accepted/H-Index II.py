# coding=utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # 利用二分法
        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            mid = low + (high - low) / 2
            if N - mid == citations[mid]:
                return citations[mid]
            elif N - mid > citations[mid]: #可能存在更大的h因子
                low = mid + 1
            else:
                high = mid - 1
        return N - low
