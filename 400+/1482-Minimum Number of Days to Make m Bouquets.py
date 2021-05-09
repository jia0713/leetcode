class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(bloomDay) < m * k:
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while(left < right):
            mid = (left + right) // 2
            if self.is_valid(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def is_valid(self, bloomDay, m, k, candi):
        res, count = 0, 0
        for flower in bloomDay:
            if flower <= candi:
                count += 1
            else:
                res += int(count / k)
                count = 0
        res += int(count / k)
        if res >= m:
            return True
        else:
            return False