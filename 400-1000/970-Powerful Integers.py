# 可能不是很好的解法
from collections import Counter


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_list, y_list = [1], [1]
        x_0, y_0 = 1, 1
        while x != 1 and x_0 < bound // x + 1:
            x_list.append(x_0 * x)
            x_0 *= x
        while y != 1 and y_0 < bound // y + 1:
            y_list.append(y_0 * y)
            y_0 *= y
        counter = Counter()
        for x_item in x_list:
            for y_item in y_list:
                if x_item + y_item <= bound:
                    counter[x_item + y_item] += 1
        return list(counter.keys())