class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        arr = [True] * n
        arr[0], arr[1] = False, False
        for i in range(int(n ** 0.5) + 1):
            if arr[i]:
                for j in range(2, (n - 1) // i + 1):
                    arr[j * i] = False
        return sum(arr)
