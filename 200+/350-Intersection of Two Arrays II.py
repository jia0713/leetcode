class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        hash_table = {}
        for num in nums2:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        for num in nums1:
            if num in hash_table and hash_table[num] != 0:
                hash_table[num] -= 1
                res.append(num)
        return res