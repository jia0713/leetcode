class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num % 9 if num % 9 != 0 or num == 0 else 9
