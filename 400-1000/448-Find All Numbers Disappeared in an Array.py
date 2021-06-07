class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            nums[abs(num) - 1] = -1 * abs(nums[abs(num) - 1])
        for index, num in enumerate(nums):
            if num > 0:
                res.append(index + 1)
        return res
