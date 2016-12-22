# coding=utf-8
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        token1=version1.split('.')
        token2=version2.split('.')
        maxlen=max(len(token1),len(token2))
        for i in range(maxlen):
            t1=0
            if i<len(token1):
                t1=int(token1[i])
            t2=0
            if i<len(token2):
                t2=int(token2[i])
            if t1!=t2:
                return 1 if t1>t2 else -1
        return 0
