class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        helper = ""
        for index in range(len(s) - 1):
            helper = helper + s[index] + "*"
        helper = helper + s[-1]
        res, maxLen = "", 0
        for index, char in enumerate(helper):
            j = 0 if index % 2 == 0 else 1
            while j <= min(index, len(helper) - index):
                if helper[index + j] == helper[index - j]:
                    if j + 1 > maxLen:
                        res, maxLen = helper[index - j : index + j + 1], j + 1
                    j += 2
                else:
                    break
        return res.replace("*", "")


if __name__ == "__main__":
    sol = Solution()
    s = "bbccbb"
    ans = sol.longestPalindrome(s)
    print(ans)
