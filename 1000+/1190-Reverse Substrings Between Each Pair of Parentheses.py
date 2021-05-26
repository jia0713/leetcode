class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char != ")":
                stack.append(char)
            else:
                p, temp = "", ""
                while p != "(":
                    temp = temp + p
                    p = stack.pop()
                for temp_c in temp:
                    stack.append(temp_c)
        res = ""
        for char in stack:
            res = res + char
        return res
