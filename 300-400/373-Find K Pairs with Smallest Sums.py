# 时间复杂度 O (k ^ 2)

import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        queue, res = [], []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                heapq.heappush(queue, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
        for _ in range(k):
            if queue:
                res.append(heapq.heappop(queue)[1])
        return res


# 优化后的版本


class Solution_2(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        queue, res = [], []
        for i in range(min(k, len(nums1))):
            heapq.heappush(queue, (nums1[i] + nums2[0], i, 0))
        while k and queue:
            cur, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < len(nums2):
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
