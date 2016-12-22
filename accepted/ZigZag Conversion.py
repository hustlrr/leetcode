# coding=utf-8
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        interval=2*numRows-2
        if numRows<=1:
            return s
        res=[]
        strlen=len(s)
        for i in range(numRows):
            j=i
            incres=[]
            if i==0 or i==numRows-1:
                incres+=[interval,interval]
            else:
                incres+=[interval-i*2,i*2]
            flag=0
            while j<strlen:
                res.append(s[j])
                j+=incres[flag]
                flag=1-flag
        return ''.join(res)
