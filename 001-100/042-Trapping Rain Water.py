class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0 or len(height) == 1:
            return 0
        res = 0
        left = [0] * len(height)
        right = [0] * len(height)
        for i in range(1, len(height)):
            left[i] = height[i - 1] if height[i - 1] > left[i - 1] else left[i - 1]
        for j in range(len(height) - 2, -1, -1):
            right[j] = height[j + 1] if height[j + 1] > right[j + 1] else right[j + 1]
        for k in range(len(height)):
            edge = min(left[k], right[k])
            if edge > height[k]:
                res += (edge - height[k])
        return res