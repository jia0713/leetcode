class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        inbound = [0] * n
        for edge in edges:
            inbound[edge[1]] += 1
        res = []
        for i in range(n):
            if inbound[i] == 0:
                res.append(i)
        return res