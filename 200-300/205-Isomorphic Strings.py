class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        pair_dict = {}
        for i, char in enumerate(s):
            if char in pair_dict:
                if pair_dict[char] != t[i]:
                    return False
            else:
                pair_dict[char] = t[i]
        pair_dict = {}
        for j, char in enumerate(t):
            if char in pair_dict:
                if pair_dict[char] != s[j]:
                    return False
            else:
                pair_dict[char] = s[j]
        return True
