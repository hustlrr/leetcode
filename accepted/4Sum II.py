# coding=utf-8
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum_A_B = {}
        for na in A:
            for nb in B:
                sum_A_B[na + nb] = sum_A_B .get(na + nb, 0) + 1
        num_combination = 0
        for nc in C:
            for nd in D:
                num_combination += sum_A_B .get(-(nc + nd), 0)
        return num_combination
