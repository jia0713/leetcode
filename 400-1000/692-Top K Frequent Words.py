import heapq
from collections import Counter


class item_dict(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        if self.value > other.value:
            return False
        if self.value < other.value:
            return True
        if self.key > other.key:
            return True
        else:
            return False


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter, res, heap = Counter(), [], []
        for word in words:
            counter[word] += 1
        for key, value in counter.items():
            pair = item_dict(key, value)
            heapq.heappush(heap, pair)

            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            res.append(heapq.heappop(heap).key)
        res.reverse()
        return res
