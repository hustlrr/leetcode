# coding=utf-8
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        num_of_words=len(words)
        words_bit=[sum([1<<(ord(c)-ord('a')) for c in set(word)]) for word in words]
        words_len=[len(word) for word in words]
        res=0
        for i in range(num_of_words):
            for j in range(num_of_words):
                if words_bit[i]&words_bit[j] ==0:
                    res=max(res,words_len[i] *words_len[j])
        return res
