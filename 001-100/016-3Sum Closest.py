class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, min_dist = float("inf"), float("inf")
        for index, num in enumerate(nums):
            left, right = index + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right] + num
                cur_dist = abs(cur_sum - target)
                if cur_dist == 0:
                    return cur_sum
                if cur_dist < min_dist:
                    res, min_dist = cur_sum, cur_dist
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    ans = sol.threeSumClosest(nums, target)
    print(ans)
