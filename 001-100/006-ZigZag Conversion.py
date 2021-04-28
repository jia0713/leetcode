class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        mod, res = 2 * numRows - 2, ""
        for i in range(min(numRows, len(s))):
            for index, char in enumerate(s):
                if index % mod == i or index % mod == (mod - i):
                    res = res + char
        return res