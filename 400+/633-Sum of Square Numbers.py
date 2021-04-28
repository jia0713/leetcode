class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(c ** 0.5)
        while left <= right:
            if left ** 2 + right ** 2 > c:
                right -= 1
            elif left ** 2 + right ** 2 < c:
                left += 1
            else:
                return True
        return False
        
class Solution_2(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        square = int(c ** 0.5)
        check_set = dict()
        for i in range(square + 1):
            check_set[i * i] = c - i * i
            if (c - i * i) in check_set:
                return True
        return False
