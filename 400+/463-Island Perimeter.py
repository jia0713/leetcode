class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        res = 0
        for i in range(1, row):
            for j in range(col):
                res += abs(grid[i][j] - grid[i-1][j])
        for j in range(1, col):
            for i in range(row):
                res += abs(grid[i][j] - grid[i][j - 1])
        for i in range(row):
            res += grid[i][0] + grid[i][-1]
        for j in range(col):
            res += grid[0][j] + grid[-1][j]
        return res