# coding=utf-8
import re
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        regex='\S*\Z'
        pattern=re.compile(regex)
        match=pattern.search(s.strip())
        if match:
            return len(match.group())
        else:
            return 0
