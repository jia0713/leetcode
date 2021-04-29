class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for value in nums:
            single ^= value
        return single


if __name__ == "__main__":
    sol = Solution()
    answer = sol.singleNumber([1, 2, 1, 3, 2])
    print(answer)
