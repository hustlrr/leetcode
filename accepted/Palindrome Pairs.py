# coding=utf-8
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_idx = {word: idx for idx, word in enumerate(words)}
        idx1_idx2 = {_: set() for _ in range(len(words))}
        for idx1, word in enumerate(words ):
            reverse = word[::-1]
            if reverse == word and '' in word_idx: # 自身是回文
                idx1_idx2[idx1].add (word_idx[''])
                idx1_idx2[word_idx['']] .add(idx1)
            if reverse in word_idx: # 自身的反字符串在数组中
                idx1_idx2[idx1].add (word_idx[reverse])
                                    idx1_idx2[word_idx[rev erse]].add(idx1)
            for leftlen in range(1, len (word)): # 都不符合就将字符串拆成左右 两部分
                left, right = word[ :leftlen], word[leftlen:]
                if left[::-1] in word_idx and right == right[ ::-1]:
                    idx1_idx2[idx1].add (word_idx[left[::-1]] )
                if right[::-1] in word_idx and left == left[::-1] :

