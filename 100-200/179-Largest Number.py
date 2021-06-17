class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums = self.quickSort(nums)
        res = "".join(nums)
        if int(res) == 0:
            return "0"
        return res

    def quickSort(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        larger, smaller = [], []
        for index in range(1, len(nums)):
            if self.isLarger(nums[index], nums[0]):
                larger.append(nums[index])
            else:
                smaller.append(nums[index])
        return self.quickSort(larger) + [nums[0]] + self.quickSort(smaller)

    def isLarger(self, a, b):
        new_a, new_b = a + b, b + a
        for index in range(len(new_a)):
            if int(new_a[index]) < int(new_b[index]):
                return False
            if int(new_a[index]) > int(new_b[index]):
                return True
        return False
