class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res, count = 0, 31
        while n != 0:
            res += 2 ** count * (n % 2)
            n = n // 2
            count -= 1
        return res