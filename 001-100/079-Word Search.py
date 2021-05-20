class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                visit = [[0] * col for _ in range(row)]
                if self.dfs(i, j, board, visit, word):
                    return True
        return False

    def dfs(self, i, j, board, visit, res_word):
        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or board[i][j] != res_word[0]
            or visit[i][j] == 1
        ):
            return False
        if len(res_word) == 1:
            return True
        visit[i][j] = 1
        res = (
            self.dfs(i + 1, j, board, visit, res_word[1:])
            or self.dfs(i - 1, j, board, visit, res_word[1:])
            or self.dfs(i, j + 1, board, visit, res_word[1:])
            or self.dfs(i, j - 1, board, visit, res_word[1:])
        )
        # 把i, j 恢复回来
        visit[i][j] = 0
        return res
