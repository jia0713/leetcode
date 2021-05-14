class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        left, right = newInterval[0], newInterval[1]
        for interval in intervals:
            if interval[1] < newInterval[0] or interval[0] > newInterval[1]:
                res.append(interval)
            else:
                if interval[1] >= newInterval[0] and interval[0] <= newInterval[0]:
                    left = interval[0]
                if interval[1] >= newInterval[1] and interval[0] <= newInterval[1]:
                    right = interval[1]
        res.append([left, right])
        res.sort()
        return res
