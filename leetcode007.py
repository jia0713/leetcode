class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        rtype = 0
        while temp!=0:
            last_digit = temp % 10
            rtype = rtype * 10 + last_digit
            temp = int(temp / 10)
        return (rtype * (1 if x>=0 else -1)) if rtype < 2**31 else 0


if __name__ == "__main__":
    sol = Solution()
    print (sol.reverse(-321))



