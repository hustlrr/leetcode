# coding=utf-8
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childs = {}
        self.isword = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for letter in word:
            p_next = p.childs.get(letter)
            if p_next is None:
                p_next = TrieNode()
                p.childs[letter] = p_next
            p = p_next
        p.isword = True

    def delwords(self, word):
        p = self.root
        nodes_del = []
        for letter in word:
            nodes_del.append((letter, p))
            p = p.childs.get(letter)
            if p is None: # 说明这个单词不存在
                return
        if len(p.childs):
            p.isword = False # 说明这个单词是其他单词的前缀
        else:
            for letter, node in nodes_del[ ::-1]:
                del node.childs[letter]
                if len(node.childs) or node .isword: # 如果和其他单词有共同前缀 ，共同前缀不应该删除
                    break


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        tree = Trie()
        for word in words:
            tree.insert(word)
        row = len(board)
        col = len(board[0]) if row else 0
        directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[False for i in range(col )] for j in range(row)]
        res = []

        def dfs(node, px, py, s):
            if px < 0 or px >= row or py < 0 or py >= col or visited[px][py]:
                return
            node = node.childs.get (board[px][py])
            if node is None:
                return
            s += board[px][py]
            if node.isword:
                res.append(s)
                tree.delwords(s) # 删除已经加入结果的单词可 以避免重复加入

            visited[px][py] = True
            for dx, dy in directs:
                dfs(node, px + dx, py + dy, s)
            visited[px][py] = False

        for px in range(row):
            for py in range(col):
                dfs(tree.root, px, py, '')
        return res
