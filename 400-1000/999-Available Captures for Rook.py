class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        row, col = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    row, col = i, j
                    break
        for j in range(col - 1, -1, -1):
            if board[row][j] == "B":
                break
            if board[row][j] == "p":
                res += 1
                break
        for j in range(col + 1, 8):
            if board[row][j] == "B":
                break
            if board[row][j] == "p":
                res += 1
                break
        for i in range(row - 1, -1, -1):
            if board[i][col] == "B":
                break
            if board[i][col] == "p":
                res += 1
                break
        for i in range(row + 1, 8):
            if board[i][col] == "B":
                break
            if board[i][col] == "p":
                res += 1
                break
        return res