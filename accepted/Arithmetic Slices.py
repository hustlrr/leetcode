# coding=utf-8
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_ = len(A)
        cnts = [0 for _ in range(len_)]
        for i in range(2, len_):
            if A[i] - A[i-1] != A[i-1] - A[i -2]:
                continue
            cnts[i] = cnts[i-1] + 1
        return sum(cnts)

