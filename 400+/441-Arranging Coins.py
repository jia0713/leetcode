class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while(left < right):
            mid = left + (right - left + 1) // 2
            mid_sum = (mid + 1) * mid // 2
            if mid_sum == n:
                return mid
            if mid_sum > n:
                right = mid - 1
            if mid_sum < n:
                left = mid
        return right