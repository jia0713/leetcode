class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs([], nums, res)
        return res

    def dfs(self, path, nums, res):
        if not nums:
            res.append(path)
            return
        nums_set = set(nums)
        for num in nums_set:
            nums_copy = [item for item in nums]
            nums_copy.remove(num)
            self.dfs(path + [num], nums_copy, res)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 3]
    ans = sol.permuteUnique(nums)
    print(ans)
