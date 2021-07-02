class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        res, cont = 0, 0
        while res < len(costs):
            cont += costs[res]
            if cont > coins:
                break
            res += 1
        return res
