class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # nums.sort()
        for index, value in enumerate(nums):
            dic = {}
            target = -1 * value
            for i in range(index + 1, len(nums)):
                if target - nums[i] in dic.values():
                    arr = [value, target - nums[i], nums[i]]
                    arr.sort()
                    if arr not in res:
                        res.append(arr)
                else:
                    dic[i] = nums[i]
        return res


if __name__ == "__main__":

    sol = Solution()
    answer = sol.threeSum([1, -1, 1, -1, 0])
    print(answer)
