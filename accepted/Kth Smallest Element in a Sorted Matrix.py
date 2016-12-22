# coding=utf-8
from heapq import heappush, heappop


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row, col = 0, 0
        if matrix:
            row, col = len(matrix), len (matrix[0])
        heap = []
        for j in range(col): # item为 (value, 行idx, 列idx)
            heappush(heap, (matrix[0][j], 0, j))
        for i in range(k - 1):
            root = heappop(heap)
            idxrow, idxcol = root[1], root[2]
            if idxrow + 1 < row:
                heappush(heap, (matrix[idxrow + 1][idxcol], idxrow + 1
