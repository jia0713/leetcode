class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for query in queries:
            cont = 0
            for point in points:
                if (point[0] - query[0]) ** 2 + (point[1] - query[1]) ** 2 <= query[
                    2
                ] ** 2:
                    cont += 1
            res.append(cont)
        return res
