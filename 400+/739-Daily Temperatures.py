class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        res, index_stack = [0] * len(T), [0]
        for i in range(1, len(T)):
            while index_stack and T[i] > T[index_stack[-1]]:
                last_index = index_stack.pop()
                res[last_index] = i - last_index
            index_stack.append(i)
        return res
