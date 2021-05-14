from collections import Counter


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        res = [0] * 2
        for i in range(1, len(nums) + 1):
            if counter[i] > 1:
                res[0] = i
            elif counter[i] == 0:
                res[1] = i
        return res
