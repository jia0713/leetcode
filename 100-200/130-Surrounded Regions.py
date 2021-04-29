class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        self.row, self.col = len(board), len(board[0])
        self.visit = [[0] * self.col for _ in range(self.row)]
        self.board = board
        for j in range(self.col):
            self.dfs(0, j)
            self.dfs(self.row - 1, j)
        for i in range(1, self.row - 1):
            self.dfs(i, 0)
            self.dfs(i, self.col - 1)
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == "O" and self.visit[i][j] == 0:
                    self.board[i][j] = "X"
        return self.board

    def dfs(self, i, j):
        if i < 0 or i > self.row - 1 or j < 0 or j > self.col - 1:
            return
        if self.board[i][j] == "X":
            return
        if self.board[i][j] == "O":
            if self.visit[i][j] == 1:
                return
            if self.visit[i][j] == 0:
                self.visit[i][j] = 1
                self.dfs(i - 1, j)
                self.dfs(i + 1, j)
                self.dfs(i, j - 1)
                self.dfs(i, j + 1)
