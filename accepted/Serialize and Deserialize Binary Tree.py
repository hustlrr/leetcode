# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
          
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def traverse(root):
            if root is None:
                res.append('#')
            else:
                res.append(str(root.val))
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return ','.join(res)
     
    def deserialize(self, data):
        """Decodes your encoded data to tree.
          
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        def constructTree():
            try:
                val = vals.next()
            except StopIteration:
                return None
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = constructTree()
            root.right = constructTree()
            return root
        vals = iter(data.split(','))
        return constructTree()
        

# Your Codec object will be instantiated and called as such:

