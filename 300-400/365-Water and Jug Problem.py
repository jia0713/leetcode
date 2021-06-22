class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity > jug2Capacity:
            jug1Capacity, jug2Capacity = jug2Capacity, jug1Capacity
        if jug1Capacity == 0:
            return jug2Capacity == targetCapacity
        while jug2Capacity % jug1Capacity != 0:
            jug1Capacity, jug2Capacity = jug2Capacity % jug1Capacity, jug1Capacity
        return targetCapacity % jug1Capacity == 0