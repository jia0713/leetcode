from collections import Counter
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = Counter()
        for num in A:
            counter[num] += 1
            if counter[num] > 1:
                return num