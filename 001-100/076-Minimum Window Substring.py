class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        maps, mapt = {}, {}
        start, count = 0, 0
        res, temp = "", 0
        for char in t:
            maps[char] = 0
            if char in mapt:
                mapt[char] += 1
            else:
                mapt[char] = 1
        for i, char in enumerate(s):
            if char in maps:
                maps[char] += 1
                if count == 0:
                    start = i
                if maps[char] <= mapt[char]:
                    count += 1
            if count == len(t):
                temp = i
                break
        if count != len(t):
            return ""
        while start <= temp:
            if s[start] not in maps:
                start += 1
            else:
                if maps[s[start]] > mapt[s[start]]:
                    maps[s[start]] -= 1
                    start += 1
                else:
                    maps[s[start]] == mapt[s[start]]
                    break
        min_length, res = temp - start + 1, s[start : temp + 1]
        for i in range(temp + 1, len(s)):
            if s[i] in maps:
                maps[s[i]] += 1
                if s[i] == s[start]:
                    while start < i:
                        if s[start] in maps:
                            if maps[s[start]] == mapt[s[start]]:
                                break
                            else:
                                maps[s[start]] -= 1
                        start += 1
                if min_length > i - start + 1:
                    min_length, res = i - start + 1, s[start : i + 1]
        return res


from collections import Counter


class Solution_2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s[0] == t:
            return t
        res, left, right, min_len = "", 0, 0, float("inf")
        counter, cur = Counter(t), Counter(s[0])
        while right < len(s) - 1:
            right += 1
            cur[s[right]] += 1
            while self.is_valid(cur, counter):
                temp = s[left : right + 1]
                if len(temp) < min_len:
                    res, min_len = temp, len(temp)
                cur[s[left]] -= 1
                left += 1
        return res

    def is_valid(self, cur, counter):
        for key in counter:
            if counter[key] > cur[key]:
                return False
        return True
