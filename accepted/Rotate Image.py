# coding=utf-8
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        for i in range(row):
            for j in range(i):
                matrix[i][j],matrix[j][i] =matrix[j][i] ,matrix[i][j]
        for i in range(row):
            matrix[i]=matrix[i][::-1]
