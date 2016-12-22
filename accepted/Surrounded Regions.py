# coding=utf-8
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0]) if row else 0

        # 边缘的字母O一定不会被包围
        # 和这些一定不会不会被包围的字母O相 邻的字母O也一定不会被包围
        stack = [pxpy for _ in range(row + col) for pxpy in ((_, 0), (_, col - 1), (0, _), (row - 1, _))]
        while stack:
            px, py = stack.pop()
            if px < row and px >= 0 and py < col and py >= 0 and board[px][py] == 'O':
                board[px][py] = '#'
                stack += [(px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)]

        # 将符号'#'换做字母'O' ,将字母'O'换做字母'X'
        for i in range(row):
            for j in range(col):
                board[i][j] = 'O' if board[i][j] == '#' else 'X'
