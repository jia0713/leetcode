class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev, temp, res = [], "", ""
        for char in s:
            if char != " ":
                temp += char
            elif temp != "":
                rev.append(temp)
                temp = ""
        if temp != "":
            rev.append(temp)
        for i in range(len(rev) - 1, 0, -1):
            res += rev[i] + " "
        if len(rev) > 0:
            res += rev[0]
        return res