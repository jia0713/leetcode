class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]:
            return ""
        prefix = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
# 容易忘掉循环走完的return
        return prefix
