# coding=utf-8
class Solution(object):
    def calcEquation(self, equations, values , query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        edges = {}
        for e, v in zip(equations, values):
            if e[0] in edges:
                edges[e[0]][e[1]] = v
            else:
                edges[e[0]] = {e[0]: 1.0, e[1]: v}
            if e[1] in edges:
                edges[e[1]][e[0]] = 1.0 / v
            else:
                edges[e[1]] = {e[1]: 1.0, e[0]: 1.0 / v}

        res = []

        def mydivide(num1, num2, path):
            if num1 not in edges or num2 not in edges:
                return -1.0
            if num2 in edges[num1]:
                return edges[num1][num2]
            for tmp in edges[num1].keys():
                tmp_value = -1.0
                if tmp not in path:
                    tmp_value = mydivide(tmp , num2, path + [tmp])
                if tmp_value and tmp_value ! = -1.0:
                    return edges[num1][tmp] * tmp_value

        for num1, num2 in query:
            _ = mydivide(num1, num2, [])
            if _:
                res.append(_)
            else:
                res.append(-1.0)
        return res
