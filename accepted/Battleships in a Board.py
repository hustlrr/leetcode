# coding=utf-8
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        cnt = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == '.':
                    continue
                if ((i == 0 and j == 0) \
                            or (i and j and board[i - 1][j] != 'X' and board[i][j - 1] != 'X') or \
                            (i and j==0 and board[i - 1][j] != 'X' ) or (i==0 and j and board[i][j - 1] != 'X' )) and \
                                board[i][j] == 'X':
                    cnt += 1
        return cnt
