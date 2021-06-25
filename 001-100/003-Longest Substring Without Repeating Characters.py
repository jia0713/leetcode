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


from collections import defaultdict


class Solution_2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = defaultdict(int)
        left, right, res = 0, 0, 0
        while right < len(s):
            if s[right] in counter:
                left = max(left, counter[s[right]] + 1)
            counter[s[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res
