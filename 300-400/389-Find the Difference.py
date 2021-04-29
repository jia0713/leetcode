class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        for letter in t:
            if letter not in s_dict or s_dict[letter] <= 0:
                return letter
            s_dict[letter] -= 1
