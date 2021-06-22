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


# 摩尔投票法，空间复杂度O(1)
class Solution_2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candi, freq = nums[0], 1
        for num in nums[1:]:
            if num == candi:
                freq += 1
            elif freq == 0:
                candi, freq = num, 0
            elif freq > 0:
                freq -= 1
        return candi
