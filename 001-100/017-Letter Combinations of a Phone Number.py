class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lett_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        for i, digit in enumerate(digits):
            if i == 0:
                for lett in lett_dict[digit]:
                    res.append(lett)
            else:
                res_temp = res.copy()
                res = []
                for lett in lett_dict[digit]:
                    for cur in res_temp:
                        res.append(cur + lett)
        return res
