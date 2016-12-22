# coding=utf-8
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        len_ = len(p)
        cnts = [0 for i in range(26)] # cnts[0]表示以'a'结尾的子字符串的 个数(即以a结尾的字符串的最大长度 )
        orderStrLen = 0
        for i in range(len_):
            if i > 0 and (ord(p[i]) - ord (p[i - 1]) == 1 or ord(p[i - 1]) - ord(p[i]) == 25):
                orderStrLen += 1
            else:
                orderStrLen = 1
            cnts[ord(p[i]) - ord('a')] = max (cnts[ord(p[i]) - ord('a')], orderStrLen)
        return sum(cnts)
