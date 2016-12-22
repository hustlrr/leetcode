# coding=utf-8
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # peakMap[i][j]表示第(i,j )个位置能有的最高水位高度
        m = len(heightMap)
        n = len(heightMap[0]) if m else 0
        peakMap = [[(1 << 31) if 0 < i < m - 1 and 0 < j < n - 1 else heightMap[i][j] for j in range (n)] for i in
                   range(m)] # 边缘没有给水，所以水位 的高度就是方块的高度
        queue = [[i, j] for i in range(m) for j in range(n) if i in (0, m - 1) or j in (0, n - 1)]
        while len(queue): # 当队列不空的时候
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            x, y = queue.pop(0)
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if not (0 < nx < m - 1 and 0 < ny < n - 1):
                    continue
                maxheight = max (heightMap[nx][ny], peakMap[x][y])
                if maxheight < peakMap[nx][ny]: # 水只会向更低的方块流动
                    peakMap[nx][ny] = maxheight
                    queue.append([nx, ny])
        return sum(peakMap[i][j] - heightMap[i][j] for i in range (m) for j in range(n))

