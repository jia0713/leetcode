from collections import Counter


class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        counter = Counter(deliciousness)
        res, mod = 0, 1e9 + 7
        for power in range(22):
            for score in set(deliciousness):
                look_up = 2 ** power - score
                if look_up in counter:
                    if look_up == score:
                        res += (0.5 * (counter[score] * (counter[score] - 1))) % mod
                    else:
                        res += (0.5 * (counter[score] * counter[look_up])) % mod
        return int(res)
