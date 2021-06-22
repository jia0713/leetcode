# 单调栈，超时

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack, res = [], 0
        helper = {}
        for index, num in enumerate(arr):
            init = index
            while stack and arr[stack[-1]] > num:
                init = stack.pop()
            if init in helper:
                helper[index] = helper[init]
            else:
                helper[index] = index
            stack.append(index)
            for start_index in stack:
                res += (start_index - helper[start_index] + 1) * arr[start_index]
                res = int(res % (1e9 + 7))
        return res
