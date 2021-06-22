class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        if turnedOn >= 9:
            return []
        res = []
        for i in range(turnedOn + 1):
            minutes, hours = [], []
            self.dfs([1, 2, 4, 8, 16, 32], 0, i, minutes)
            self.dfs([1, 2, 4, 8], 0, turnedOn - i, hours)
            for hour in hours:
                for minute in minutes:
                    if hour < 12 and minute < 60:
                        res.append("{}:{:0>2d}".format(hour, minute))
        return res

    def dfs(self, arr, cur, num, res):
        if len(arr) < num:
            return
        if num == 0:
            res.append(cur)
        else:
            self.dfs(arr[1:], cur + arr[0], num - 1, res)
            self.dfs(arr[1:], cur, num, res)


if __name__ == "__main__":
    sol = Solution()
    turnedOn = 1
    ans = sol.readBinaryWatch(turnedOn)
    print(ans)
