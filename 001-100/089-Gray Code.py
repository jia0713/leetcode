class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            temp = res[::-1]
            for item in temp:
                res.append(item + 2 ** i)
        return res
