# coding=utf-8
class Solution(object):
    def longestIncreasingPath(self, matrix ):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        height = len(matrix)
        if height:
            width = len(matrix[0])
        else:
            return 0
        dp = [[0] * width for i in range (height)]
        directs = [(1,0),(-1,0),(0,1),(0 ,-1)]
        def dfs(px, py):
            if dp[px][py]:
                return dp[px][py]
            for dx, dy in directs:
                cx, cy = px + dx, py + dy
                if cx >=0 and cx < height and cy >= 0 and cy < width and matrix[cx][cy] < matrix[px][py]:
                    dp[px][py] = max (dp[px][py], dfs(cx, cy))
            dp[px][py] += 1
            return dp[px][py]

