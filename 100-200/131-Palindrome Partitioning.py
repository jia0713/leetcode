class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j]判断i,j之间是否是回文字符串
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j or (s[i] == s[j] and j - i <= 2):
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if dp[i + 1][j - 1]:
                        dp[i][j] = True
        res = []
        self.dfs(0, [], dp, s, res)
        return res

    def dfs(self, curr, path, dp, s, res):
        if curr > len(s):
            return
        if curr == len(s):
            res.append(path)
            return
        for j in range(curr, len(s)):
            if dp[curr][j]:
                path_copy = [item for item in path]
                path_copy.append(s[curr: j + 1])
                self.dfs(j + 1, path_copy, dp, s, res)


if __name__ == "__main__":
    sol = Solution()
    s = "aabbcca"
    ans = sol.partition(s)
    print(ans)
