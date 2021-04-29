class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        temp = ""
        for char in s:
            if char.isalnum():
                temp = temp + char
        return temp == temp[::-1]
