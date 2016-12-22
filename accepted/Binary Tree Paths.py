# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root==None:
            return []
        if root.left==None and root.right ==None:
            return [str(root.val)]
        ret=[]
        left=self.binaryTreePaths(root.left)
        right=self.binaryTreePaths(root .right)
        cur=str(root.val)
        for s in left+right:
            ret.append(cur+'->'+s)
        return ret
