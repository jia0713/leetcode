'''给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。'''

class Solution:

    def twoSum(self, nums, target):
        dic = {}
        for index, value in enumerate(nums):
            if value in dic.keys():
                return [dic[value], index]
            dic[target - value] = index

if __name__ == '__main__':

    nums = [1, 3, 6, 9]
    target = 10
    solution = Solution()
    assert (solution.twoSum(nums, target)==[0, 3])










