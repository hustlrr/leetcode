# coding=utf-8
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnts=[0 for i in range(128)]
        cntt=[0 for i in range(128)]
        idx=0
        for cs,ct in zip(s,t):
            if cnts[ord(cs)]!=cntt[ord(ct)]:
                return False
            cnts[ord(cs)]=idx+1
            cntt[ord(ct)]=idx+1
            idx+=1
        return True
