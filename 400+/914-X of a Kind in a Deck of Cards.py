from collections import Counter


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        counter = Counter()
        for item in deck:
            counter[item] += 1
        count_list = list(counter.values())
        divisor = min(count_list)
        while divisor > 1:
            count_list = [
                item - divisor if item != divisor else item for item in count_list
            ]
            if count_list == [divisor] * len(count_list) or not count_list:
                return True
            divisor = min(count_list)
        return False
