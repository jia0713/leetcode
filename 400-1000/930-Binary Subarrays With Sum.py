from collections import Counter


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        res, cont = 0, 0
        counter = Counter({0: 1})
        for num in nums:
            cont += num
            counter[cont] += 1
        for i in range(sum(nums) - goal + 1):
            if goal == 0:
                res += (counter[i] * (counter[i] - 1)) // 2
            else:
                res += counter[i] * counter[i + goal]
        return res
