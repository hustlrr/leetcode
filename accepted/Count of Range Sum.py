# coding=utf-8
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)

        def mergeSort(start, end):
            mid = start + (end - start) / 2
            if mid == start:
                return 0
            cnt = mergeSort(start, mid) + mergeSort(mid, end)
            i = j = mid
            for idxleft in range(start, mid):
                while i < end and sums[i] - sums[idxleft] < lower:
                    i += 1
                while j < end and sums[j] - sums[idxleft] <= upper:
                    j += 1
                cnt += (j - i)
            sums[start:end] = sorted
