class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {}
        for char in s:
            if char not in hash_table:
                hash_table[char] = 1
            else:
                hash_table[char] += 1
        for index, char in enumerate(s):
            if hash_table[char] == 1:
                return index
        return -1
