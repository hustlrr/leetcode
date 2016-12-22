# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret=[]
        x=[]
        if root: x.append(root)
        while len(x):
            ret.append([node.val for node in x])
            tmp=[]
            for node in x:
                if node.left: tmp.append (node.left)
                if node.right: tmp.append (node.right)
            x=tmp
        return ret
        
