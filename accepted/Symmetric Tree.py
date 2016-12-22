# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def help(self,rx,ry):
        if rx==None and ry==None:
            return True
        else:
            return rx!=None and ry!=None and rx.val==ry.val and \
        self.help(rx.left,ry.right) and self .help(rx.right,ry.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root==None or self.help(root .left,root.right)
