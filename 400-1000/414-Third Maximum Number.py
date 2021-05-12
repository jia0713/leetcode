class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = []
        for num in nums:
            if num not in window:
                window.append(num)
                window.sort(reverse=True)
            if len(window) > 3:
                window.pop()
        if len(window) < 3:
            return window[0]
        return window[-1]