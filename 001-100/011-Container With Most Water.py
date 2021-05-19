class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                h, w = height[left], right - left
                left += 1
            else:
                h, w = height[right], right - left
                right -= 1
            res = max(res, h * w)
        return res
