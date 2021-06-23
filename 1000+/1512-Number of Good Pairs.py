from collections import Counter


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        counter = Counter(nums)
        for value in counter.values():
            res += value * (value - 1) // 2
        return res
