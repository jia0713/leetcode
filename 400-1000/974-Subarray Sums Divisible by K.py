from collections import Counter


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter, res, remain = Counter({0: 1}), 0, 0
        for num in nums:
            remain = (remain + num) % k
            res += counter[remain]
            counter[remain] += 1
        return res
