class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        self.dfs([], candidates, target)
        return self.res

    def dfs(self, path, candidates, target):
        if not candidates or target < candidates[0]:
            return
        if target == candidates[0]:
            self.res.append(path + [candidates[0]])
            return
        self.dfs(path + [candidates[0]], candidates, target - candidates[0])
        self.dfs(path, candidates[1:], target)
