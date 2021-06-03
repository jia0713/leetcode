class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count, hash_table = 0, 0, {0: -1}
        for index, num in enumerate(nums):
            count = count - 1 if num == 0 else count + 1
            if count in hash_table:
                res = max(res, index - hash_table[count])
            else:
                hash_table[count] = index
        return res
