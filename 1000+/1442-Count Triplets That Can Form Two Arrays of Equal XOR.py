class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        helper = [0] * (len(arr) + 1)
        for i in range(1, len(helper)):
            helper[i] = helper[i - 1] ^ arr[i - 1]
        for i in range(len(helper) - 1):
            for j in range(i + 1, len(helper)):
                if helper[i] == helper[j]:
                    res += j - i - 1
        return res
