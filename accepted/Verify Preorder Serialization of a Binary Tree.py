# coding=utf-8
class Solution(object):
    def isValidSerialization(self, preorder ):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        degree = -1 #一颗合法的二叉树的入度要比出度大 1，因为任何一个出度都是另一个节 点的入度，例外是根节点，这里我们 假设根节点也有入度
        for node in nodes:
            degree += 1 
            if degree > 0:
                return False
            elif node != '#': 
                degree -= 2
        return degree == 0
