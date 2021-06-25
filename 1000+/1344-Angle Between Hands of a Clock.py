class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour = hour % 12
        angle_1 = (minutes - hour * 5) * 6
        angle_2 = 5 * 6 * minutes / 60.0
        angle = angle_1 - angle_2
        return angle if angle <= 180 else 360 - angle
