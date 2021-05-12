class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res, flag = "", 0
        for i in range(max(len(num1), len(num2))):
            if i < len(num1) and i < len(num2):
                cur = int(num1[len(num1) - i - 1]) + int(num2[len(num2) - i - 1]) + flag
            elif i >= len(num1):
                cur = int(num2[len(num2) - i - 1]) + flag
            elif i >= len(num2):
                cur = int(num1[len(num1) - i - 1]) + flag
            flag = cur // 10
            cur_string = str(cur % 10)
            res = cur_string + res
        if flag:
            res = str(flag) + res
        return res
