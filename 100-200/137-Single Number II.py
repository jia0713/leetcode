class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = (sum(3 * list(set(nums))) - sum(nums)) // 2
        return res
