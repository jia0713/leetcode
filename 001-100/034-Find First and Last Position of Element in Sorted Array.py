class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right -= 1
            if nums[mid] < target:
                left += 1
            if nums[mid] == target:
                if nums[left] == target and nums[right] == target:
                    return [left, right]
                if nums[left] < target:
                    left += 1
                if nums[right] > target:
                    right -= 1
        return [-1, -1]
