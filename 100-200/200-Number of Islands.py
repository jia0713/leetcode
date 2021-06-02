class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.res = 0
        self.grid = grid
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if self.grid[i][j] == "1":
                    self.res += 1
                    self.dfs(i, j)
        return self.res

    def dfs(self, i, j):
        row, col = len(self.grid), len(self.grid[0])
        if i < 0 or i >= row or j < 0 or j >= col or self.grid[i][j] != "1":
            return
        self.grid[i][j] = "*"
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)
