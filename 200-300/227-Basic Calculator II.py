class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s + "+"
        cur, flag = 0, "+"
        stack = []
        for char in s:
            if char == " ":
                continue
            if char.isdigit():
                cur = 10 * cur + int(char)
            else:
                if flag == "+":
                    cur = cur
                if flag == "-":
                    cur = -1 * cur
                if flag == "*" or flag == "/":
                    last_num = stack.pop()
                    if flag == "*":
                        cur = cur * last_num
                    if flag == "/":
                        if last_num >= 0:
                            cur = last_num // cur
                        else:
                            cur = -(-last_num // cur)
                stack.append(cur)
                flag, cur = char, 0
                cur = 0
        return sum(stack)
