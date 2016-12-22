# coding=utf-8
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            if root.left:
                root.left.next=root.right
            if root.right and root.next:
                root.right.next=root.next .left
            self.connect(root.left)
            self.connect(root.right)
