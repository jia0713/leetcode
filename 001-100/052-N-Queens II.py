class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = 0
        queens = [-1] * n
        self.put(queens, 0)
        return self.res

    def isValid(self, queens, i, j):
        for index, queen in enumerate(queens):
            if queen != -1:
                if abs(index - i) == abs(queen - j) or j == queen:
                    return False
        return True

    def put(self, queens, i):
        if i == len(queens):
            self.res += 1
            return
        for j in range(len(queens)):
            if self.isValid(queens, i, j):
                queens[i] = j
                self.put(queens, i + 1)
                queens[i] = -1
