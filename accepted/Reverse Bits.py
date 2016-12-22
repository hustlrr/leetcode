# coding=utf-8
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask=1<<31
        ret=0
        for i in range(32):
            ret+=(mask*(n&1))
            n>>=1
            mask>>=1
        return ret
