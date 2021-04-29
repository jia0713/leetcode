class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == nums[0]:
            return 0
        bp = 0
        while bp < len(nums) - 1:
            if nums[bp] > nums[bp + 1]:
                break
            bp += 1
        if target > nums[0]:
            left, right = 0, bp
        else:
            left, right = bp + 1, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return -1
