class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = grid
        self.island = 0
        self.row, self.col = len(self.grid), len(self.grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == "1":
                    self.island += 1
                    self.dfs(i, j)
        return self.island

    def dfs(self, i, j):
        if i < 0 or i >= self.row or j < 0 or j >= self.col:
            return
        if self.grid[i][j] == "1":
            self.grid[i][j] = "*"
            self.dfs(i - 1, j)
            self.dfs(i + 1, j)
            self.dfs(i, j - 1)
            self.dfs(i, j + 1)
        else:
            return
