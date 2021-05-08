class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        count, label = 0, nums[left]
        while left <= right:
            if nums[left] == label:
                count += 1
            else:
                label = nums[left]
                count = 1
            if count > 2:
                temp = nums[left]
                for index in range(left, right):
                    nums[index] = nums[index + 1]
                nums[right] = temp
                right -= 1
            else:
                left += 1
        return right + 1
