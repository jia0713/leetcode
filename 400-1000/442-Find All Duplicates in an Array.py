class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for index, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            nums[abs(num) - 1] = -nums[abs(num) - 1]
        return res
