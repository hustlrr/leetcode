# coding=utf-8
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        row, col = len(matrix), len (matrix[0]) if len(matrix) else 0
        self.sum = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0:
                    self.sum[i][j] = self .sum[i][j - 1] + self .matrix[i][j]
                elif j == 0:
                    self.sum[i][j] = self .sum[i - 1][j] + self .matrix[i][j]
                else:
                    self.sum[i][j] = self .sum[i - 1][j] + self .sum[i][j - 1] - self .sum[i - 1][j - 1] + self.matrix[i][
                        j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1 )..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.sum[row2][col2]
        elif row1 == 0:
            return self.sum[row2][col2] - self.sum[row2][col1 - 1]
        elif col1 == 0:
            return self.sum[row2][col2] - self.sum[row1 - 1][col2]
        else:
            return self.sum[row2][col2] - self.sum[row1 - 1][col2] - self.sum[row2][col1 - 1] \
                   + self.sum[row1 - 1][col1 - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)

