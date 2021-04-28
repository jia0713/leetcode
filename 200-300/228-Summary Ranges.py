class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        left, right, res = 0, 0, []
        while(left < len(nums)):
            while (right < len(nums) and (right - left == nums[right] - nums[left])):
                right += 1
            if right - left == 1:
                res.append(str(nums[left]))
            else:
                res.append(str(nums[left]) + "->" + str(nums[right-1]))
            left = right
        return res