class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_sum, digit_product = 0, 1
        while n > 0:
            n, rest = n // 10, n % 10
            digit_sum += rest
            digit_product *= rest
        return digit_product - digit_sum
