class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs([], nums)
        return self.res

    def dfs(self, path, left):
        if len(left) == 0:
            self.res.append(path)
            return
        for item in left:
            self.dfs(path + [item], list(set(left) - set([item])))
