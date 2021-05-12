class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        res = 1
        left, right, cur = 0, 0, nums[0]
        while right < len(nums):
            if nums[right] * (right - left + 1) - cur <= k:
                res = max(res, right - left + 1)
                if right + 1 < len(nums):
                    right += 1
                    cur += nums[right]
                else:
                    break
            else:
                cur -= nums[left]
                left += 1
        return res
