class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            if target > matrix[i][-1]:
                continue
            else:
                left, right = 0, col
                while left < right:
                    mid = left + (right - left) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                return False
