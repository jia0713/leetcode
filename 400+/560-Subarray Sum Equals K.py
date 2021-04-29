class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_table, res, count = {0: 1}, 0, 0
        for i, num in enumerate(nums):
            count += num
            if count - k in hash_table:
                res += hash_table[count - k]
            if count in hash_table:
                hash_table[count] += 1
            else:
                hash_table[count] = 1
        return res
