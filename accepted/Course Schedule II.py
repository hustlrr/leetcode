# coding=utf-8
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 初始化
        adjs = [set() for i in range (numCourses)]
        indegree = [0 for i in range (numCourses)]
        for nx, ny in prerequisites:
            if nx in adjs[ny]: #注意输入中可能会有重复的边 ，此时入度不能重复计算
                continue
            adjs[ny].add(nx)
            indegree[nx] += 1
        vertices = [1 for i in range (numCourses)]
        res = []
        while True:
            disposeNodes = [i for i in range (numCourses) if vertices[i] and indegree[i] == 0]
            if len(disposeNodes) == 0:
                break
            for ny in disposeNodes:
                for nx in adjs[ny]:
                    indegree[nx] -= 1
                adjs[ny].clear()
                vertices[ny] = 0
                res.append(ny)
        res.extend([i for i in range (numCourses) if vertices[i]])
        return res if sum(indegree) == 0 else []
