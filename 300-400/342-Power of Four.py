class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0) and (1073741824 % num == 0) and (num - 1) % 3 == 0
