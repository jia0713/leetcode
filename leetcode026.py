class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[flag]:
                nums[flag + 1] = nums[i]
                flag += 1
        return flag + 1, nums

if __name__ == "__main__":
    sol = Solution()
    print (sol.removeDuplicates([1, 1, 1]))
