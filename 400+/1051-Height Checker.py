class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights_copy = [x for x in heights]
        heights_copy.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i] != heights_copy[i]:
                res += 1
        return res