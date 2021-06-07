# 经典的0-1背包问题

class Solution:
    def findTargetSumWays(self, nums, S):
        sum_nums = sum(nums)
        if sum_nums < S or (S + sum_nums) % 2 != 0:
            return 0
        target = (S + sum_nums) // 1
        mem = [0] * (target + 1)
        mem[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                mem[i] += mem[i - num]
        return mem[target]


# 二维DP矩阵，dp[i][j]代表前j个数之和为i的可能总数
# dp[i][j] =dp[i-num[j]][j-1] + dp[i][j-1]


class Solution_2(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nums_sum = sum(nums)
        if (nums_sum - S) % 2 != 0 or nums_sum < S:
            return 0
        target = (nums_sum - S) // 2
        dp = [[0] * (len(nums) + 1) for _ in range(nums_sum + 1)]
        dp[0][0] = 1
        for i in range(nums_sum + 1):
            for j in range(1, len(nums) + 1):
                if i >= nums[j - 1]:
                    dp[i][j] = dp[i - nums[j - 1]][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[target][-1]
