class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        for index, char in enumerate(s):
            if char == "0":
                if s[index - 1] != "1" and s[index - 1] != "2":
                    return 0
                dp[index + 1], dp[index] = dp[index - 1], dp[index - 1]
            if char != "0":
                if s[index - 1] == "0":
                    dp[index + 1] = dp[index]
                elif index >= 1 and int(s[index - 1 : index + 1]) > 26:
                    dp[index + 1] = dp[index]
                elif index >= 1:
                    dp[index + 1] = dp[index] + dp[index - 1]
        return dp[-1]
