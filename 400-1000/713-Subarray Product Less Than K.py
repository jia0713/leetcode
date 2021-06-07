class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j, res, count = 0, 1, 0
        for i in range(len(nums)):
            res *= nums[i]
            if res >= k:
                while j <= i and res >= k:
                    res /= nums[j]
                    j += 1
            count += i - j + 1
        return count
