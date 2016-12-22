# coding=utf-8
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idxa=len(a)-1
        idxb=len(b)-1
        sum=''
        carray=0
        while idxa>=0 or idxb>=0:
            x=int(a[idxa]) if idxa>=0 else 0
            y=int(b[idxb]) if idxb>=0 else 0
            sum=str((x+y+carray)%2)+sum
            carray=(x+y+carray)/2
            idxa-=1
            idxb-=1
        return sum if carray==0 else str (carray)+sum
