# 二分法 时间复杂度 O(NlogN)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return 1
        left, right = 1, len(nums) - 1
        while left < right:
            count, mid = 0, (left + right) // 2
            for i in range(len(nums)):
                if nums[i] < mid:
                    count += 1
            if count < mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
