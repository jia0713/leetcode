class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        count = 0
        while left <= right or top <= bottom:
            # 向右
            i, j = top, left
            while j <= right:
                count += 1
                res[i][j] = count
                j += 1
            top += 1
            # 向下
            i, j = top, right
            while i <= bottom:
                count += 1
                res[i][j] = count
                i += 1
            right -= 1
            # 向左
            i, j = bottom, right
            while j >= left:
                count += 1
                res[i][j] = count
                j -= 1
            bottom -= 1
            i, j = bottom, left
            while i >= top:
                count += 1
                res[i][j] = count
                i -= 1
            left += 1
        return res
