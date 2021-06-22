# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            my_guess = left + (right - left) // 2
            if guess(my_guess) == 0:
                return my_guess
            if guess(my_guess) == 1:
                left = my_guess + 1
            if guess(my_guess) == -1:
                right = my_guess
        return left
