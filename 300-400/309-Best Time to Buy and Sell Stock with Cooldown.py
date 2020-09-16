# 这道题的关键就是定义状态和状态之间的转移
# 状态是hold, sold, rest 三种
# 这三种状态是如何相互转移的
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rest, sold, hold = 0, 0, -float("inf")
        for price in prices:
            pre_rest = rest
            rest = max(rest, sold)
            sold = hold + price
            hold = max(hold, pre_rest - price)
        return max(sold, rest)