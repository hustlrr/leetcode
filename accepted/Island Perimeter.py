# coding=utf-8
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        height, width = len(grid), len (grid[0])
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0: # 该区域是水域
                    continue
                for dx, dy in directs:
                    if dx + i < 0 or dx + i >= height or \
                                                                  dy + j < 0 or dy + j >= width:
                        perimeter += 1
                        continue
                    if grid[dx + i][dy + j] == 0:
                        perimeter += 1
        return perimeter

