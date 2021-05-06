from collections import Counter


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = Counter()
        for stone in stones:
            counter[stone] += 1
        res = 0
        for jewel in jewels:
            res += counter[jewel]
        return res
