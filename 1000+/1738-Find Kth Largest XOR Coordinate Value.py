import heapq


class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        helper = [[0] * col for _ in range(row)]
        for j in range(col):
            helper[0][j] = matrix[0][j]
            for i in range(1, row):
                helper[i][j] = helper[i - 1][j] ^ matrix[i][j]
        queue = []
        for i in range(row):
            cur = 0
            for j in range(col):
                cur ^= helper[i][j]
                heapq.heappush(queue, cur)
                if len(queue) == k + 1:
                    heapq.heappop(queue)
        while len(queue) > k:
            heapq.heappop(queue)
        return queue[0]
