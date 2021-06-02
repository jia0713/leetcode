# 自己的解法
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        max_day = max(days) + 31
        hold = [float("inf")] * max_day
        buy_1 = [float("inf")] * max_day
        buy_7 = [float("inf")] * max_day
        buy_30 = [float("inf")] * max_day
        buy_1[days[0]], buy_7[days[0]], buy_30[days[0]] = costs[0], costs[1], costs[2]
        last_day_cost = float("inf")
        for index in range(1, len(days)):
            day, last_day = days[index], days[index - 1]
            last_day_cost = min(
                hold[last_day], buy_1[last_day], buy_7[last_day], buy_30[last_day]
            )
            buy_1[day] = last_day_cost + costs[0]
            buy_7[day] = last_day_cost + costs[1]
            buy_30[day] = last_day_cost + costs[2]
            for i in range(last_day + 1, last_day + 7):
                hold[i] = min(hold[i], buy_7[last_day])
            for i in range(last_day + 1, last_day + 30):
                hold[i] = min(hold[i], buy_30[last_day])
        return min(hold[days[-1]], buy_1[days[-1]], buy_7[days[-1]], buy_30[days[-1]])


# 剪枝以后的版本
class Solution_2(object):
    def mincostTickets(self, days, costs):
        m = max(days)
        dp = [0] * (m + 1)
        days = set(days)
        for i in range(1, m + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    costs[0] + dp[i - 1],
                    costs[1] + dp[max(0, i - 7)],
                    costs[2] + dp[max(0, i - 30)],
                )
        return dp[-1]
