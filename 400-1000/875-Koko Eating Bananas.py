class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            mid_time = self.count_hours(piles, mid)
            if mid_time > H:
                left = mid + 1
            if mid_time <= H:
                right = mid
        return left

    def count_hours(self, piles, K):
        res = 0
        for pile in piles:
            res += (pile - 1) // K + 1
        return res