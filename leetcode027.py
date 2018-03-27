class Solution:

    def removeElements(self, nums, val):
        i = 0
        flag = 0
        while i <= len(nums) - 1:
            if nums[i] != val:
                temp = nums[i]
                nums[flag] = nums[i]
                nums[i] = temp
                flag += 1
            i += 1
        print (flag)
        return nums


if __name__ == "__main__":
    sol = Solution()
    answer = sol.removeElements([3], val=3)
    print(answer)

