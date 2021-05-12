class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        total = 0
        for i in range(len(encoded) + 1):
            total ^= i + 1
        first = total
        for i in range(1, len(encoded) + 1, 2):
            first ^= encoded[i]
        res, cur = [], first
        for i in range(len(encoded)):
            res.append(cur)
            cur ^= encoded[i]
        res.append(cur)
        return res
