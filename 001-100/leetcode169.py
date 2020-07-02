class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for item in nums:
            dic[item] = dic[item] + 1 if item in dic.keys() else 1
        for key, value in dic.items():
            if value > len(nums) / 2:
                return key


if __name__ == "__main__":
    sol = Solution()
    answer = sol.majorityElement([1, 3, 1, 3, 3, 3])
    print (answer)

