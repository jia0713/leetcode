# 思考下面几个问题：
# 1. 结束递归的条件
# 2. queens数组初始化为-1是否能够表示所有皇后冲突，并且不产生误报冲突
# 3. 重新搜索，用queens[i] = -1 这一行代表
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
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
            temp_res = []
            for queen in queens:
                temp_res.append("." * queen + "Q" + "." * (len(queens) - 1 - queen))
            self.res.append(temp_res)
            return
        for j in range(len(queens)):
            if self.isValid(queens, i, j):
                queens[i] = j
                self.put(queens, i + 1)
                queens[i] = -1
