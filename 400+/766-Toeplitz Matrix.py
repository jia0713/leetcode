class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        for i in range(col):
            for j in range(min(row, col - i)):
                if matrix[j][i+j] != matrix[0][i]:
                    return False
        for i in range(1, row):
            for j in range(min(row-i, col)):
                if matrix[i+j][j] != matrix[i][0]:
                    return False
        return True