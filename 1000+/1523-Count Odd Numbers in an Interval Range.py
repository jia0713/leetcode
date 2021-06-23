class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (low % 2 - 1) * (high % 2 - 1) == 0:
            return (high - low) // 2 + 1
        else:
            return (high - low) // 2
