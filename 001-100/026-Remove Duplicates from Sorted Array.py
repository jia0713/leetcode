class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        flag, count = -float('inf'), 0
        for index, num in enumerate(nums):
            if num > flag:
                nums[count] = num
                count += 1
                flag = num
        return count