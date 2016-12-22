# coding=utf-8
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pair={}
        words=str.split()
        if len(pattern)!=len(words):
            return False
        for c,word in zip(pattern,words):
            try:
                if pair[c]!=word:
                    return False
            except KeyError:
                if word in pair.values():
                    return False
                pair[c]=word
        return True
