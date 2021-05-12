from collections import defaultdict


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        counter = defaultdict(int)
        for index, num in enumerate(nums2):
            counter[num] = index
        for num in nums1:
            index = counter[num] + 1
            while index < len(nums2):
                if nums2[index] > num:
                    res.append(nums2[index])
                    break
                index += 1
            if index >= len(nums2):
                res.append(-1)
        return res
