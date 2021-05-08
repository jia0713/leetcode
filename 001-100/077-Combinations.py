class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs([], 1, n, k)
        return self.res

    def dfs(self, path, cur, n, k):
        if k == 0:
            self.res.append(path)
            return
        if n - cur + 1 == k:
            self.res.append(path + list(range(cur, cur + k)))
            return
        self.dfs(path + [cur], cur + 1, n, k - 1)
        self.dfs(path, cur + 1, n, k)
