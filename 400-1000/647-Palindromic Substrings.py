class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and j - i <= 2:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                if dp[i][j]:
                    res += 1
        return res
