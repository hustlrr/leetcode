# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getNums(self, root, path):
        if root is None:
            yield 0
        if root:
            path.append(root.val)
            if root.right is None and root .left is None:
                yield int(''.join([str(i) for i in path]))
            if root.left:
                for num in self.getNums(root .left,path):
                    yield num
            if root.right:
                for num in self.getNums(root .right,path):
                    yield num
            path.pop()

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums=[]
        for num in self.getNums(root,[]):
            nums.append(num)
        return sum(nums)
