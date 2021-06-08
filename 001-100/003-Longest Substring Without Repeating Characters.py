class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        start = 0
        max_length = min(1, len(s))
        current_length = 0
        for i in range(0, len(s)):
            if s[i] in dic.keys() and start <= dic[s[i]]:
                start = dic[s[i]] + 1
            else:
                current_length = i - start + 1
            max_length = max(current_length, max_length)
            dic[s[i]] = i
        return max_length

