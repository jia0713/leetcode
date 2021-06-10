class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        left, right, cur = 0, 0, 0
        while right < len(gas):
            cur += gas[right] - cost[right]
            if cur < 0:
                left, cur = right + 1, 0
                right = left
            else:
                right += 1
        return left
