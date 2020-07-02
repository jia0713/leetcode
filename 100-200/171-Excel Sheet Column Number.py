class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(0, len(s)):
            res += (ord(s[len(s) - 1 -i]) - 64) * pow(26, i)
        return res