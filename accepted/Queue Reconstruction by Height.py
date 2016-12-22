# coding=utf-8
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people = sorted(people, key=lambda x : x[1]) # 身高相同时根据前面更高的人数顺序 排序
        people = sorted(people, reverse=True , key=lambda x: x[0]) # 根据身高逆序排序

        res = []
        for h, k in people:
            res.insert(k, [h, k])
        return res
