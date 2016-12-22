# coding=utf-8
import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        ans = None
        M, N = max(row, col), min(row, col ) # 以下的注释都假设行数大于列数
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                ordersums, num = [], 0
                for z in range(M):
                    sums[z] += matrix[z][y] if row > col else matrix[y][z] # 如果行大于列，sums[z] 记录的是(0, x)到(z, y )的和
                    num += sums[z] # num记录这个矩阵块的和
                    idx = bisect .bisect_left (ordersums, num - k) # 寻找num - k插入的位置 ,因为这个位置左边到该 坐标的和一定大于k
                    if idx != len (ordersums): # idx == len(ordersums )的情况在if num<= k这个条件中处理
                        ans = max(ans, num - ordersums[idx])

