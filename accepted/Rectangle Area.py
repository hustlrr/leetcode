# coding=utf-8
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        res=(C-A)*(D-B)+(G-E)*(H-F)
        #没有重叠部分
        if E>C or G<A or H<B or F>D:
            return res
        else:
            leftx=max(A,E)
            lefty=max(B,F)
            rightx=min(C,G)
            righty=min(D,H)
            return res-(rightx-leftx )*(righty-lefty)
