# coding=utf-8
class Solution(object):
    def fullJustify(self, words, maxWidth ):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        startidx = 0
        while startidx < len(words):
            endidx, len_ = startidx, 0
            while endidx < len(words) and len_ + len(words[endidx]) + endidx - startidx <= maxWidth: # 计算这行可以放多少个单词
                len_ += len(words[endidx])
                endidx += 1
            out, num_of_words, num_of_space = '', endidx - startidx, maxWidth - len_
            for k in range(startidx, endidx):
                out += words[k]
                tmp = 0
                if num_of_space > 0:
                    if endidx != len(words ): # 不是最后一行
                        if endidx - k > 1: # 不是该行最后一空格
                            if num_of_space % (endidx - k - 1) == 0 :
                                tmp = num_of_space / (endidx - k - 1)
                            else:
                                tmp = num_of_space / (endidx - k - 1) + 1
                        else:
                            tmp = num_of_space
                    else:
                        if endidx - k == 1 :
                            tmp = num_of_space
                        else:

