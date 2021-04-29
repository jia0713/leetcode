class Solution:
    def getSqure(self, nums):
        res = 0
        while nums != 0:
            res += pow((nums % 10), 2)
            nums = int(nums / 10)
        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        index = 0
        res = self.getSqure(n)
        dic = {}
        while res not in dic:
            dic[index] = res
            index += 1
            res = self.getSqure(res)
        return True if res == 1 else False


if __name__ == "__main__":
    sol = Solution()
    answer = sol.isHappy(86)
    print(answer)
