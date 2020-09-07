import heapq
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        heap = []
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
        count = 0
        while(heap):
            count += 1
            neg_score, i = heapq.heappop(heap)
            if count == 1:
                res[i] = "Gold Medal"
            elif count == 2:
                res[i] = "Silver Medal"
            elif count == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(count)
        return res