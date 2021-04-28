class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left, right = 1, num
        while(left < right):
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                left = mid + 1
            if mid * mid > num:
                right = mid
        return False