class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 1:
            return False
        if s == s[0] * length:
            return True
        divisors = []
        for i in range(2, int(length ** 0.5) + 1):
            if length % i == 0:
                divisors.append(i)
        for divisor in divisors:
            res = length / divisor
            if s == s[:divisor] * res or s == s[:res] * divisor:
                return True
        return False
