# coding=utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=len(matrix)
        col=0
        if row: col=len(matrix[0])
        for x in range(row):
            y=col-1
            while y and matrix[x][y]>target:
                y-=1
            if matrix[x][y]==target:
                return True
        return False
