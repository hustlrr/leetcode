# coding=utf-8
class Solution(object):
    def bfs(self, q, visited, canArrive, matrix):
        '''
        :type q: List[List[int]]
        :type visited: List[List[int]]
        :type canArrive: List[List[int]]
        :type matrix: List[List[int]]
        :return: 
        '''
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        while len(q):
            x, y = q.pop(0)
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    continue
                if matrix[nx][ny] >= matrix[x][y]:
                    q.append([nx, ny])
                    canArrive[nx][ny] = True
                    visited[nx][ny] = True
        return canArrive

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        # 先利用bfs求解可以到达pacific的节点
        visited = [[False if i and j else True for j in range(n)] for i in range(m)]
        canArrivePacific = [[False if i and j else True for j in range(n)] for i in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    q.append([i, j])
        self.bfs(q, visited, canArrivePacific, matrix)
        # 再用bfs求解可以到达Atlantic的节点
        visited = [[False if i != m-1 and j != n-1 else True for j in range (n)] for i in range(m)]
        canArriveAtlantic = [[False if i != m-1 and j != n-1 else True for j in range(n)] for i in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if i == m -1 or j == n-1:
                    q.append([i, j])
        self.bfs(q, visited, canArriveAtlantic, matrix)
        res = []
        for i in range(m):
            for j in range(n):
                if canArriveAtlantic[i][j] and canArrivePacific[i][j]:
                    res.append([i, j])
        return res
