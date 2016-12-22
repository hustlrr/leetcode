# coding=utf-8
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in -place instead.
        """
        #邻近的活细胞数目是2、3时，活的细 胞可以继续存活，其他情况活细胞 会死亡
        #邻近的活细胞数目是3时，死细胞会复 活，其他情况死细胞状态不变
        row,col=len(board),0
        if row: col=len(board[0])
        directs=[(-1,-1),(-1,0),(-1,1),(0 ,-1),(0,1),(1,-1),(1,0),(1,1)]
        for x in xrange(row):
            for y in xrange(col):
                cur_state=board[x][y]&1
                lives_neighbor=0
                for direct in directs:
                    if x+direct[0]>=row or x+direct[0]<0 or y +direct[1]>=col or y +direct[1]<0:
                        continue
                    lives_neighbor +=board[x +direct[0]][y +direct[1]]&1
                if ((cur_state==1 and (lives_neighbor==2 or lives_neighbor==3))
                or (cur_state==0 and lives_neighbor==3)):
                    board[x][y]|=2

