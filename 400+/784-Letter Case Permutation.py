class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for char in S:
            candi = []
            if char.isalpha():
                candi = [char.lower(), char.upper()]
            else:
                candi = [char]
            temp = [string for string in res]
            res = []
            for string in temp:
                for char in candi:
                    res.append(string + char)
        res = list(set(res))
        return res 