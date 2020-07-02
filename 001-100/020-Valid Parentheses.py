class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        par_dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in range(len(s)):
            if s[i] not in par_dict:
                stack.append(s[i])
	#不要忘记栈为空的情况
            elif not stack:
                return False
            elif stack.pop() != par_dict[s[i]]:
                return False
        return False if stack else True
