class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        queue, res = [], []
        for index, char in enumerate(s):
            if char == c:
                queue.append(index)
        queue.append(float("inf"))
        left, right = -float("inf"), queue.pop(0)
        for index in range(len(s)):
            if index > right:
                left = right
                right = queue.pop(0)
            res.append(min(index - left, right - index))
        return res
