class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low, high = 0, len(S)
        res = [0] * (len(S) + 1)
        for index, char in enumerate(S):
            if char == "I":
                res[index] = low
                low += 1
            if char == "D":
                res[index] = high
                high -= 1
        res[-1] = high