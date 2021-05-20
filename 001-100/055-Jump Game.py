class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i, num in enumerate(nums):
            if i <= max_reach:
                max_reach = max(max_reach, num + i)
            if max_reach >= len(nums) - 1:
                return True
        return False
