# coding=utf-8
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens, lenp = len(s), len(p)
        recs, recp, idxs, idxp = -1, -1, 0 , 0
        while idxs < lens:
            if idxp < lenp and (s[idxs] == p[idxp] or p[idxp] == '?' ): # 匹配s中的当前字符与p中 *后面的字符，如果匹配，则在 这个if中处理
                idxs += 1
                idxp += 1
            elif idxp < lenp and p[idxp] == '*': # 如果不匹配，则继续比较s中的 下一个字符
                recp = idxp
                idxp += 1
                recs = idxs
            elif recp != -1:
                idxp = recp + 1
                recs += 1
                idxs = recs
            else:
                return False
        while idxp < lenp and p[idxp] == '
