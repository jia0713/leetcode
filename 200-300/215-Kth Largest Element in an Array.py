import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        queue = []
        for num in nums:
            heapq.heappush(queue, num)
            if len(queue) == k + 1:
                heapq.heappop(queue)
        return queue[0]
