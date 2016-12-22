# coding=utf-8
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            maskrow=[False for k in range (9)]
            maskcol=[False for k in range (9)]
            for j in range(9):
                if board[i][j]!='.':
                    tmp=int(board[i][j])-1
                    if maskrow[tmp]==False : maskrow[tmp] =True
                    else: return False
                if board[j][i]!='.':
                    tmp=int(board[j][i])-1
                    if maskcol[tmp]==False : maskcol[tmp]=True
                    else: return False
        mask=[[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.': continue
                if board[i][j] in mask[i /3][j/3]:
                    return False
                else:

