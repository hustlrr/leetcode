# coding=utf-8
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        s, res, lastsum = sum(A), sum([idx * num for idx, num in enumerate(A )]),sum([idx * num for idx, num in enumerate(A)])
        len_ = len(A)
        for i in range(1, len(A)):
            lastsum = lastsum + s - A[-i] * (len_)
            res = max(res, lastsum)
        return res
