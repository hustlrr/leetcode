# coding=utf-8
from collections import defaultdict


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        dp = [0 for _ in range(n)]
        jumpUnits = defaultdict(set)
        jumpUnits[0].add(0)
        k = 0
        for i in range(1, n):
            while dp[k] + 1 < stones[i] - stones[k]:
                k += 1
            for j in range(k, i):
                dist = stones[i] - stones[j]
                if (dist - 1) in jumpUnits[j] or dist in jumpUnits[j] or \
                                (dist + 1) in jumpUnits[j]:
                    jumpUnits[i].add(dist)
                    dp[i] = max(dp[i], dist)
        return len(jumpUnits[n - 1]) != 0
