# coding=utf-8
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrimes=[True]*max(n,2)
        isPrimes[0]=False
        isPrimes[1]=False
        i=2
        while i*i<n:
            if isPrimes[i]:
                j=i*i
                while j<n:
                    isPrimes[j]=False
                    j+=i
            i+=1
        return sum(isPrimes)
