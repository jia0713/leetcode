class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left, right, mid = 0, x, x // 2
        while(True):
            if left == right or left == right - 1:
                return mid
            if mid * mid > x:
                right = mid
                mid = (left + mid) // 2
            if mid * mid <= x:
                left = mid
                mid = (mid + right) // 2