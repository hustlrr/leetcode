# coding=utf-8
class Solution(object):
    def getRC(self,idx,col):
        x=idx/col
        y=idx%col
        return x,y

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low=0
        row,col=len(matrix),0
        if row:
            col=len(matrix[0])
        high=row*col-1
        while low<=high:
            mid=low+(high-low)/2
            midx,midy=self.getRC(mid,col)
            if matrix[midx][midy]==target:
                return True
            elif matrix[midx][midy]<target:
                low=mid+1
            else:
                high=mid-1
        return False
