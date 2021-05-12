class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.upper()
        whole = ""
        for char in s:
            if char.isalnum():
                whole = whole + char
        mod = len(whole) % k if len(whole) % k != 0 else k
        head, rest = whole[:mod], whole[mod:]
        if not rest:
            return head
        ans = head
        for index in range(len(rest) // k):
            ans = ans + "-"
            ans = ans + rest[index * k : (index + 1) * k]
        return ans
