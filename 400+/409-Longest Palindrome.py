from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter, res = Counter(), 0
        for char in s:
            counter[char] += 1
        for key in counter:
            res += counter[key] // 2 * 2
            counter[key] -= counter[key] // 2 * 2
        for key in counter:
            if counter[key] != 0:
                return res + 1
        return res
