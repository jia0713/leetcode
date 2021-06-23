# odd, even 代表以当前数结尾的奇数，偶数子数组的个数
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odd, even, res = 0, 0, 0
        for num in arr:
            if num % 2 == 0:
                odd, even = odd, even + 1
            else:
                odd, even = even + 1, odd
            res = (res + odd) % (1e9 + 7)
        return int(res)
