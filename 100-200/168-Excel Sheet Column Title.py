class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        while columnNumber != 0:
            columnNumber, rest = columnNumber // 26, columnNumber % 26
            if rest == 0:
                rest, columnNumber = 26, columnNumber - 1
            res = chr(64 + rest) + res
        return res
