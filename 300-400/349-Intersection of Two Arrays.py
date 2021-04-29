from collections import Counter


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter, res = Counter(), []
        for num in nums1:
            counter[num] += 1
        for num in nums2:
            if num in counter:
                res.append(num)
        res = list(set(res))
        return res
