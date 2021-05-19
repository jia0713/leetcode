class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.dfs(n, n, "")
        return self.res

    def dfs(self, left, right, path):
        if right < left or left < 0:
            return
        if left == 0 and right == 0:
            self.res.append(path)
            return
        self.dfs(left - 1, right, path + "(")
        self.dfs(left, right - 1, path + ")")
