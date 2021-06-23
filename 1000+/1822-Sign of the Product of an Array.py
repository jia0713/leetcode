class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cont = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                cont += 1
        return 1 if cont % 2 == 0 else -1
