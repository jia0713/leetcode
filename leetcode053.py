class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = nums[0]
        flag_max = nums[0]
        for index in range(1, len(nums)):
            flag_max = max(flag_max + nums[index], nums[index])
            current_max = max(current_max, flag_max)
            index += 1
        return current_max


if __name__ == "__main__":
    sol = Solution()
    answer = sol.maxSubArray([-1, 3])
    print(answer)






