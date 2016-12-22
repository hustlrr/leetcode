# coding=utf-8
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value=[1000,900,500,400,100,90,50,40 ,10,9,5,4,1]
        symbol=['M','CM','D','CD','C','XC' ,'L','XL','X','IX','V','IV','I']
        res=''
        for v,s in zip(value,symbol):
            len=1
            while len*v<=num:
                len+=1
                res+=s
            num-=v*(len-1)
        return res
