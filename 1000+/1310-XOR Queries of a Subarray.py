class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        helper = [0] * (len(arr) + 1)
        helper[1] = arr[0]
        for i in range(2, len(helper)):
            helper[i] = helper[i - 1] ^ arr[i - 1]
        res = [0] * len(queries)
        for index, [p, q] in enumerate(queries):
            res[index] = helper[p] ^ helper[q + 1]
        return res
