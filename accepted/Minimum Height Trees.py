# coding=utf-8
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adjs = [set() for i in range(n)]
        for nx, ny in edges:
            adjs[nx].add(ny)
            adjs[ny].add(nx)
        vertices = [1 for i in range(n)]
        while sum(vertices) > 2:
            # 叶子节点
            leaves = [i for i in range(n) if vertices[i] and len(adjs[i]) == 1]
            for nx in leaves: # 去掉叶子节点的邻接点
                for ny in adjs[nx]:
                    adjs[ny].remove(nx)
                vertices[nx] = 0
        return [i for i in range(n) if vertices[i]]
