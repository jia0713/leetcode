class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        res = ""
        abs_num = abs(num)
        while(abs_num > 0):
            res = str(abs_num % 7) + res
            abs_num = abs_num // 7
        if num < 0:
            res = "-" + res
        return res