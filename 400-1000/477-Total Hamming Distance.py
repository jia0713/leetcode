class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for _ in range(31):
            temp = 0
            for index, num in enumerate(nums):
                temp += num % 2
                nums[index] = num >> 1
            res += temp * (len(nums) - temp)
        return res
