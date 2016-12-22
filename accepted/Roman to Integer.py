# coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r2d={'I':1,'V':5,'X':10,'L':50,'C' :100,'D':500,'M':1000}
        res=r2d[s[-1]]
        for i in range(len(s)-1):
            if r2d[s[i]]<r2d[s[i+1]]:
                res-=r2d[s[i]]
            else:
                res+=r2d[s[i]]
        return res
