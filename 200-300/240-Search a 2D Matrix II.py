class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if matrix:
            row,col,width=len(matrix)-1,0,len(matrix[0])
            while row>=0 and col<width:
                if matrix[row][col]==target:
                    return True
                elif matrix[row][col]>target:
                    row=row-1
                else:
                    col=col+1
            return False

# 二分查找，效率较慢
class Solution_2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        cur_row, right = 0, col
        while(cur_row < row):
            if matrix[cur_row][0] > target:
                return False
            if matrix[cur_row][-1] == target:
                return True
            if matrix[cur_row][-1] < target:
                cur_row += 1
            else:
                res = self.searchRow(matrix[cur_row], target, 0, right)
                if matrix[cur_row][res] == target:
                    return True
                right = res
                cur_row += 1
        return False
            
    def searchRow(self, matrix_row, target, left, right):
        while(left < right):
            mid = left + (right - left + 1) // 2
            if matrix_row[mid] == target:
                return mid
            if matrix_row[mid] > target:
                right = mid - 1
            if matrix_row[mid] < target:
                left = mid
        return left