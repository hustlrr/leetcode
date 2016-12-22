# coding=utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<1:
            return ''
        idx_len={idx:len(s) for idx,s in enumerate(strs)}
        idx_len=sorted(idx_len.iteritems (),key=lambda x:x[1])
        min_idx,min_len=idx_len[0]
        res=''
        for i in range(min_len):
            for s in strs:
                if s[i]!=strs[min_idx][i]:
                    return res
            res+=strs[min_idx][i]
        return res
