class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nums = list(range(0, rowIndex + 1))
        nums[0] = 1
        for i in range(1, rowIndex + 1):
            temp = 1
            nums[i] = 1
            for j in range(1, i):
                value = temp + nums[j]
                temp = nums[j]
                nums[j] = value
        return nums


if __name__ == "__main__":
    sol = Solution()
    answer = sol.getRow(rowIndex=5)
    print (answer)


