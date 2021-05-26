class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        start, res = float("inf"), 0
        stack = []
        current = 0
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            if char == ")":
                if not stack:
                    start = i + 1
                else:
                    current = stack.pop()
                    if not stack:
                        start = min(start, current)
                        res = max(res, i - start + 1)
                    else:
                        current = stack[-1]
                        res = max(res, i - current)
        return res


# DP + stack
class Solution_2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
                dp[i] = 0
            if char == ")":
                if not stack:
                    dp[i] = 0
                else:
                    j = stack.pop()
                    if j >= 1:
                        dp[i] = i - j + 1 + dp[j - 1]
                    else:
                        dp[i] = i - j + 1
        return max(dp)


class Solution_3(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, res = [], 0
        helper = [-float("inf")] * len(s)
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")" and stack:
                left_index = stack.pop()
                helper[index] = index - left_index + 1
                if left_index >= 1 and helper[left_index - 1] > 0:
                    helper[index] = helper[index] + helper[left_index - 1]
                res = max(res, helper[index])
        return res
