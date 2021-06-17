import heapq
from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter, queue, res = Counter(s), [], ""
        for key, value in counter.items():
            heapq.heappush(queue, (-value, key))
        while queue:
            item = heapq.heappop(queue)
            value, key = -1 * item[0], item[1]
            res = res + key * value
        return res
