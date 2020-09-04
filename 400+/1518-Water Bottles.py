class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        cur, res = numBottles, numBottles
        while(cur >= numExchange):
            res += cur // numExchange
            cur = cur % numExchange + cur // numExchange
        return res