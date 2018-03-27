class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        for i in range(0, len(nums)-1):
            if nums[i] == target:
                return i
            if nums[i] < target and nums[i+1] >= target:
                return i + 1
            i += 1
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    answer = sol.searchInsert([1, 2, 4, 6, 7], target=3)
    print(answer)

