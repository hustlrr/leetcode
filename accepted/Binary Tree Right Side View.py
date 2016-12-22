# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        queue=[root] if root is not None else []
        while len(queue):
            tmp=[]
            for idx,node in enumerate (queue):
                if idx==0:
                    res.append(node.val)
                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)
            queue=tmp

