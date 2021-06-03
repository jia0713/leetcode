class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        left, right, res = 0, 0, float("inf")
        count = nums[0]
        while (right < len(nums)) and (left <= right):
            if count < target:
                right += 1
                if right < len(nums):
                    count += nums[right]
            else:
                res = min(res, right - left + 1)
                count -= nums[left]
                left += 1
        return res
