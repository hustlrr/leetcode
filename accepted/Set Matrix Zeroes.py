# coding=utf-8
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row,col=len(matrix),0
        if row:
            col=len(matrix[0])
        rowFlag=all(i!=0 for i in matrix[0])
        colFlag=all(matrix[i][0]!=0 for i in range(row))
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        for i in range(col):
            matrix[0][i]*=rowFlag
        for j in range(row):
            matrix[j][0]*=colFlag
