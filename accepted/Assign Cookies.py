# coding=utf-8
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)

        contentChild = 0
        # g\s按照从小到大排序
        gidx, sidx = 0, 0
        while sidx < len(s) and gidx < len(g ):
            if s[sidx] >= g[gidx]: # 当前size可以满足这个孩子
                gidx += 1
                contentChild += 1
            sidx += 1
        return contentChild

