# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt=0
        stack=[]
        while root or len(stack):
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                cnt+=1
                if cnt==k:
                    return root.val
                root=root.right
