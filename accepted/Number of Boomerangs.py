# coding=utf-8
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        num_boomerange = 0
        for idx, px in enumerate(points):
            dist_cnt = {}
            for idy, py in enumerate(points ):
                if idx == idy:
                    continue
                d = (px[0] - py[0]) * (px[0] - py[0]) + (px[1] - py[1]) * (px[1] - py[1])
                dist_cnt[d] = dist_cnt.get(d , 0) + 1
            for cnt in dist_cnt.values():
                num_boomerange += cnt * (cnt - 1) # A(cnt, 2),排列数
        return num_boomerange
