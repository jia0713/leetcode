class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if dp[i] != 1 and coin < i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != float("inf") else -1


# 剪枝之后的算法
class Solution_2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != float("inf") else -1


# 广度优先搜索
class Solution_3(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        coins = set(coins)
        res, queue, visited = 0, [amount], set()
        while queue:
            res += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr in visited:
                    continue
                for coin in coins:
                    if curr == coin:
                        return res
                    if curr > coin:
                        queue.append(curr - coin)
                        visited.add(curr)
        return -1
