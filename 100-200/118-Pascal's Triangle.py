class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        alist = list(range(0, numRows))
        if numRows > 0:
            alist[0] = [1]
            for i in range(1, numRows):
                blist = list(range(0, i + 1))
                blist[0] = alist[i - 1][0]
                blist[i] = alist[i - 1][-1]
                for j in range(1, i):
                    blist[j] = alist[i - 1][j - 1] + alist[i - 1][j]
                alist[i] = blist
        return alist


if __name__ == "__main__":
    sol = Solution()
    answer = sol.generate(numRows=5)
    print(answer)
