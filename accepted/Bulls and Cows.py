# coding=utf-8
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull=[0 for i in range(10)]
        cnts=[0 for i in range(10)]
        cntg=[0 for i in range(10)]
        for s,g in zip(secret,guess):
            if s==g:
                bull[ord(s)-ord('0')]+=1
            cnts[ord(s)-ord('0')]+=1
            cntg[ord(g)-ord('0')]+=1
        cow=[min(cs,cg)-b for b,cs,cg in zip (bull,cnts,cntg)]
        return '%dA%dB'%(sum(bull),sum(cow))
