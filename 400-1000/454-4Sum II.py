from collections import Counter


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        counter, res = Counter(), 0
        for num_1 in nums1:
            for nums_2 in nums2:
                counter[-(num_1 + nums_2)] += 1
        for num_3 in nums3:
            for num_4 in nums4:
                res += counter[num_3 + num_4]
        return res
