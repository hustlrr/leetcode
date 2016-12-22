# coding=utf-8
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        edges = [[] for j in range (numCourses)]
        for ex, ey in prerequisites:
            edges[ey].append(ex)
            indegree[ex] += 1
        # 去掉入度为0的节点
        disposeNodes = [i for i in range (numCourses) if indegree[i] == 0]
        while len(disposeNodes) != 0:
            for nodey in disposeNodes:
                for nodex in edges[nodey]:
                    indegree[nodex] -= 1
                edges[nodey] = []
            disposeNodes = []
            for ny in range(numCourses):
                if indegree[ny] == 0 and len(edges[ny]) != 0:

