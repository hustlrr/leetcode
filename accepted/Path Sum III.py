# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum_(self, root, sum, target, prior_sum):
        if root is None:
            return 0
        sum += root.val
        res = prior_sum.get(sum - target, 0)
        prior_sum[sum] = prior_sum.get(sum, 0) + 1
        res += (self.pathSum_(root.left, sum , target, prior_sum) + \
               self.pathSum_(root.right, sum , target, prior_sum))
        prior_sum[sum] = prior_sum.get(sum) - 1
        return res

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.pathSum_(root, 0, sum, {0: 1})


