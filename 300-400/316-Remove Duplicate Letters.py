# 贪心 + 单调栈
# 用一个Counter统计字符频率
# 用一个set记录当前字符是否在前面出现过
from collections import Counter


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter, stack, visited = Counter(s), ["0"], set({})
        for char in s:
            if char not in visited:
                while ord(stack[-1]) > ord(char) and counter[stack[-1]] > 0:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)
            counter[char] -= 1
        stack.pop(0)
        return "".join(stack)
