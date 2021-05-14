class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res, cur = [], intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= cur[1]:
                cur = [cur[0], max(cur[1], interval[1])]
            else:
                res.append(cur)
                cur = interval
        res.append(cur)
        return res
