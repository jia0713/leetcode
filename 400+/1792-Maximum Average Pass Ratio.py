import heapq


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        que, res = [], 0
        for [p, t] in classes:
            gain = p / t - (p + 1) / (t + 1)
            heapq.heappush(que, (gain, p, t))

        while que:
            gain, p, t = heapq.heappop(que)
            if extraStudents > 0:
                p, t = p + 1, t + 1
                gain = p / t - (p + 1) / (t + 1)
                heapq.heappush(que, (gain, p, t))
                extraStudents -= 1
            else:
                res += p / t
        return res / len(classes)


