# coding=utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        sumlen=len(haystack)
        sublen=len(needle)
        for ih,ch in enumerate(haystack):
            if sumlen-ih>=sublen and haystack[ih:ih+sublen] ==needle:
                return ih
        return -1 if haystack!=needle else 0
