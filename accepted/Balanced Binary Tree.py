# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self,root):
        if root:
            return max(self.height(root.left ),\
                       self.height(root .right))+1
        else: return 0
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None or (root.left==None and root.right==None):
            return True
        return self.isBalanced(root.right) and \
    self.isBalanced(root.left) and \
    -1<=self.height(root.left)-self.height (root.right)<=1
