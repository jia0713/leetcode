class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, res = [], ""
        for index, char in enumerate(s):
            if char == " ":
                stack.reverse()
                res += "".join(stack) + " "
                stack = []
            else:
                stack.append(char)
        if stack:
            stack.reverse()
            res += "".join(stack)
        return res
