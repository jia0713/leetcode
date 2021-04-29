class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        sum = min(height[i], height[j]) * (j - i)
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            sum = max(sum, min(height[i], height[j]) * (j - i))
        return sum


if __name__ == "__main__":
    sol = Solution()
    answer = sol.maxArea([1, 2, 4, 3, 2, 6, 7])
    print(answer)
