class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        flag = 0
        for index in range(len(nums) - 1, 0, -1):
            flag = index
            if nums[index] > nums[index - 1]:
                break
        if flag != 1:
            temp = nums[flag - 1]
            nums[flag - 1] = nums[flag]
            nums[flag] = temp
        if flag == 1:
            flag = 0
        end = len(nums) - 1
        while flag < end:
            for index in range(flag, end):
                if nums[index] > nums[index + 1]:
                    temp = nums[index + 1]
                    nums[index + 1] = nums[index]
                    nums[index] = temp
            end -= 1
        return nums
