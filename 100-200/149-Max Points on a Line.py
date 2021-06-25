from collections import Counter


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res, MAX = 0, 1e9 + 7
        line_dict = Counter()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[j][0] == points[i][0]:
                    slope, b = MAX, points[i][0]
                else:
                    slope = (points[j][1] - points[i][1]) / (
                        points[j][0] - points[i][0]
                    )
                    b = points[i][1] - slope * points[i][0]
                slope, b = round(slope, 8), round(b, 8)
                line_dict[(slope, b)] += 1
                res = max(res, line_dict[(slope, b)])
        return int(0.5 * (1 + 8 * res) ** 0.5 + 1)
