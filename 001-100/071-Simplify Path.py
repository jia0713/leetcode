# 没想到用split"/",这个方法就非常巧妙了


class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for i in path.split("/"):
            if i not in ["", ".", ".."]:
                stack.append(i)
            elif i == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)
