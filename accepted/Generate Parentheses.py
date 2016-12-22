# coding=utf-8
class Solution(object):
    def path(self,res,curpath,left,right):
        '''
        left:目前的左括号数
        right:目前的右括号数
        '''
        if left==right and left==0:
            res.append(curpath)
            return
        if left>=right:
            #余下的左括号数目大于等于右括号 数目的时候只能加入左括号
            curpath+='('
            self.path(res,curpath,left-1 ,right)
        else:
            if left:
                self.path(res,curpath+'(' ,left-1,right)
            if right:
                self.path(res,curpath+')' ,left,right-1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        curpath=''
        self.path(res,curpath,n,n)
        return res
