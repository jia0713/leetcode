import heapq


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        queue, res = [], []
        for num in arr:
            heapq.heappush(queue, Item(abs(num - x), num))
        while k and queue:
            res.append(heapq.heappop(queue).b)
            k -= 1
        res.sort()
        return res


class Item(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a < other.a:
            return True
        if self.a > other.a:
            return False
        if self.b <= other.b:
            return True
        return False
