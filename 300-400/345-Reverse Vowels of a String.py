class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "AEIOUaeiou"
        i, j = 0, len(s) - 1
        res = list(s)
        while i < j:
            while i <= len(s) - 1 and s[i] not in vowels:
                i += 1
            while j >= 0 and s[j] not in vowels:
                j -= 1
            if i >= j:
                break
            temp = res[j]
            res[j] = res[i]
            res[i] = temp
            i += 1
            j -= 1
        ans = ""
        for char in res:
            ans += char
        return ans
