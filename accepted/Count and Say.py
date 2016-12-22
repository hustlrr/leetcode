# coding=utf-8
class Solution(object):
    def count(self,s):
        cur='#'
        cnt=0
        res=''
        s+='#'
        for c in s:
            if c!=cur:
                if cur!='#':
                    res+=str(cnt)+cur
                cur=c
                cnt=1
            else:
                cnt+=1
        return res

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res='1'
        for i in range(1,n):
            # print res
            res=self.count(res)
        return res
