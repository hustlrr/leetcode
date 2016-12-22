# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.subTreeSum(root, False)

    def subTreeSum(self, root, isLeft):
        '''
        :param root: 子树的根节点
        :param isLeft: 左子树为True，右子树为False
        :return:
        '''
        if root and root.left is None and root.right is None: # root是叶子节点
            return root.val if isLeft else 0
        if root:
            return self.subTreeSum(root.left , True) + self.subTreeSum (root.right, False)
        else:
            return 0

