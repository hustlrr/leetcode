# coding=utf-8
import Queue


class Solution(object):
    def __init__(self):
        self.res = []
        self.adjwords = []
        self.distance = {}

    def buildEdges(self, length, wordlist): # 得到那两个词之间可以互相转换
        for i in range(length):
            adjs = {}
            for word in wordlist:
                entry = word[:i] + word[i + 1:]
                words = adjs.get(entry, [])
                words.append(word)
                adjs[entry] = words
            self.adjwords.append(adjs)

    def getNextWord(self, word): # 得到与词语word相邻的词语
        nextwords = []
        for i in range(len(word)):
            entry = word[:i] + word[i + 1:]
            adjs = self.adjwords[i].get (entry, [])
            for nextword in adjs:
                if nextword != word:
                    nextwords.append (nextword)
        return nextwords

    def BFS(self, beginWord):
        queue = Queue.Queue()
        self.distance[beginWord] = 0
        queue.put(beginWord)
        while not queue.empty():
            wordx = queue.get()
            for wordy in self.getNextWord (wordx):
                if wordy in self.distance:
                    continue
                self.distance[wordy] = self .distance[wordx] + 1
                queue.put(wordy)

    def DFS(self, cur, target, path):
        if cur == target:
            self.res.append(path[:])
            return
        for nextword in self.getNextWord(cur ):
            if self.distance[nextword] - 1 == self.distance[cur]:
                self.DFS(nextword, target, path + [nextword])

    def findLadders(self, beginWord, endWord , wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if beginWord is None or endWord is None or \
                        len(beginWord) != len(endWord) or \
                        beginWord not in wordlist or \
                        endWord not in wordlist: \
                return self.res
        self.buildEdges(len(beginWord), wordlist)
        self.BFS(beginWord)
        if beginWord in self.distance:
            self.DFS(beginWord, endWord, [beginWord])
        return self.res
