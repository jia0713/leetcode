class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        l = int(area ** 0.5)
        while l <= area:
            if area % l == 0:
                return (max(l, area // l), min(l, area // l))
            l += 1
