class Solution(object):
    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        div = set([1])
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                div.add(i)
                div.add(num // i)
        return sum(div) == num
