class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = str(i)
        for i in range(n // 3 + 1):
            res[3 * i] = "Fizz"
        for i in range(n // 5 + 1):
            if res[5 * i] == "Fizz":
                res[5 * i] = "FizzBuzz"
            else:
                res[5 * i] = "Buzz"
        res.pop(0)
        return res
