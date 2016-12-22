# coding=utf-8
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp=set()
        while n!=1:
            if n in tmp: return False
            tmp.add(n)
            digits=[]
            while n:
                digits.append((n%10)*(n%10))
                n/=10
            n=sum(digits)
        return True
