class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        self.backtracking(0, candidates, target, [])
        return self.res

    def backtracking(self, index, candidates, target, path):
        if index >= len(candidates) or candidates[index] > target:
            return
        if candidates[index] == target:
            self.res.append(path + [candidates[index]])
        self.backtracking(
            index, candidates, target - candidates[index], path + [candidates[index]]
        )
        self.backtracking(index + 1, candidates, target, path)
