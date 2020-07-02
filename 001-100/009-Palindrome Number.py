class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        strs = str(x)
        l, r = 0, len(strs) - 1
        while(l < r):
            if strs[l] != strs[r]:
                return False
            l += 1
            r -= 1
        return True