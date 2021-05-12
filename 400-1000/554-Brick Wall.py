from collections import Counter
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counter = Counter()
        for line in wall:
            count = 0
            for brick in line:
                counter[count + brick] += 1
                count += brick
        counter[sum(wall[0])] = 0
        return len(wall) - counter.most_common()[0][1]