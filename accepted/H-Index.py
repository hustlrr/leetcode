# coding=utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N=len(citations) #数组中的文章数
        citation_num=[0]*(N+1)
        for c in citations:
            citation_num[[N,c][N>c]]+=1
        for i in range(N,0,-1):
            if citation_num[i]>=i:
                return i
            citation_num[i-1] +=citation_num[i]
        return 0
