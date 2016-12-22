# coding=utf-8
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnts=[0 for i in range(128)]
        cntt=[0 for i in range(128)]
        for c in s:
            cnts[ord(c)]+=1
        for c in t:
            cntt[ord(c)]+=1
        for cs,ct in zip(cnts,cntt):
            if cs!=ct:
                return False
        return True
