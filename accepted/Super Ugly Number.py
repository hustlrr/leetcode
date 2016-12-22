# coding=utf-8
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res=[1]
        factor_idx={prime:0 for prime in primes}
        for i in range(1,n):
            tmp={}
            for factor,idx in factor_idx .items():
                tmp[factor]=factor*res[idx]
            nextUgly=min(tmp.values())
            res.append(nextUgly)
            for factor,mul in tmp.items():
                if mul==nextUgly:
                    factor_idx[factor]+=1
        return res[-1]
