# coding=utf-8
from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 欧拉路径
        edges = defaultdict(list)
        for start, end in sorted(tickets)[ ::-1]:
            edges[start].append(end)
        route, stack = [], ['JFK']
        while stack:
            while edges[stack[-1]]:
                stack.append(edges[stack[ -1]].pop())
            route.append(stack.pop())
        return route[::-1]

