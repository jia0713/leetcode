class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue, res = [], []
        for index, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(index)
            if index >= k - 1:
                if index - queue[0] > k - 1:
                    queue.pop(0)
                res.append(nums[queue[0]])
        return res
