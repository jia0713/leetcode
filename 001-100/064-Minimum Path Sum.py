class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        dp = [[float("inf")] * (col + 1) for _ in range(row + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if i != 1 or j != 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[-1][-1]
