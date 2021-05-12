class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        while(g and s):
            if g[-1] <= s[-1]:
                res += 1
                g.pop()
                s.pop()
            else:
                s.pop()
        return res