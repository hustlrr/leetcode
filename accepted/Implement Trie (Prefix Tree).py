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

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for letter in word:
            p = p.childs.get(letter)
            if p is None:
                return False
        return p.isword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for letter in prefix:
            p = p.childs.get(letter)
            if p is None:
                return False
        return True
