from collections import Counter


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counter = Counter(moves)
        if counter["U"] == counter["D"] and counter["L"] == counter["R"]:
            return True
        return False
