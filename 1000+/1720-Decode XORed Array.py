class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first] * (len(encoded) + 1)
        for index, item in enumerate(encoded):
            res[index + 1] = first ^ item
            first = res[index + 1]
        return res
