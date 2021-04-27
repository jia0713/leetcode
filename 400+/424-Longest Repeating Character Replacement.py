from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, right, res = 0, 0, 0
        counter = collections.Counter()
        while right < len(s):
            counter[s[right]] += 1
            while right - left + 1 - counter.most_common(1)[0][1] > k:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res