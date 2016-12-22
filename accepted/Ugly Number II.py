# coding=utf-8
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[1]
        factor_idx={2:0,3:0,5:0}
        for i in range(1,n):
            tmp={2:0,3:0,5:0}
            for factor,idx in factor_idx .items():
                tmp[factor]=factor*res[idx]
            minUgly=min(tmp.values())
            for factor,mul in tmp.items():
                if mul==minUgly:
                    factor_idx[factor]+=1
            res.append(minUgly)
        return res[-1]
