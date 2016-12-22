# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def yes_or_no(self,root):
        yes,no=0,0 #抢劫当前节点获得的收益和不抢劫获 得的收益
        if root:
            left=self.yes_or_no(root.left)
            right=self.yes_or_no(root.right)
            #抢劫了当前节点，则不能再抢劫左 子树的根节点和右子树的根节点
            yes+=(left[1]+right[1])+root.val
            #不抢劫当前节点
            no+=(max(left)+max(right))
        return yes,no

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        yes,no=self.yes_or_no(root)
        return max(yes,no)
