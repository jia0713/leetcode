class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        split = s.split(" ")
        res = 0
        for word in split:
            if word != "":
                res += 1
        return res
