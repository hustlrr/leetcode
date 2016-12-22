# coding=utf-8
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        flag=1
        res=0
        for idx,c in enumerate(str):
            if idx==0:
                if c=='-':
                    flag=-1
                elif c=='+':
                    flag=1
                elif c.isdigit():
                    res=res*10+(ord(c)-ord ('0'))
                else:
                    return res
                continue
            if not c.isdigit():
                if flag==1:
                    return res*flag if res <=((1<<31)-1) else ((1 <<31)-1)*flag
                else:
                    return res*flag if res <=(1<<31) else (1<<31 )*flag
            res=res*10+(ord(c)-ord('0'))
        if flag==1:
            return res*flag if res<=((1<<31 )-1) else ((1<<31)-1)*flag
        else:
            return res*flag if res<=(1<<31) else (1<<31)*flag
