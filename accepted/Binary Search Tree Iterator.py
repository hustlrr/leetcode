# coding=utf-8
# Definition for a binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self.cur=root

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)!=0 or self .cur!=None

    def next(self):
        """
        :rtype: int
        """
        while self.cur:
            self.stack.append(self.cur)
            self.cur=self.cur.left
        self.cur=self.stack.pop()
        res=self.cur.val
        self.cur=self.cur.right
        return res
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
