# 完全背包问题
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        candis, sqrt = [], int(n ** 0.5)
        for num in range(1, sqrt + 1):
            candis.append(num * num)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for candi in candis:
            for i in range(n - candi + 1):
                dp[i + candi] = min(dp[i + candi], dp[i] + 1)
        return dp[-1]


# 广度优先搜索
class Solution_2(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue, res = [n], 0
        squares = [x ** 2 for x in range(1, int(n ** 0.5) + 1)]
        while True:
            queue_copy = [s for s in queue]
            queue = []
            while queue_copy:
                num = queue_copy.pop()
                for item in squares:
                    if item == num:
                        return res + 1
                    if item < num:
                        queue.append(num - item)
                    else:
                        continue
            res += 1
