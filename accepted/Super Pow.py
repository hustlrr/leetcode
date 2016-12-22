# coding=utf-8
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MASK = 1337
        res, mul = 1, a
        for num in b[::-1]:
            res = (res * ((mul ** num) % MASK)) % MASK
            mul = (mul ** 10) % MASK
        return res
