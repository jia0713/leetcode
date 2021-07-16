class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res, max_change, mod = 0, 0, 1e9 + 7
        helper = [num for num in nums1]
        helper.sort()
        for index in range(len(nums2)):
            curr = abs(nums1[index] - nums2[index])
            res += curr
            min_diff = self.findMinDiff(helper, nums2[index])
            max_change = max(max_change, curr - min_diff)
        return int((res - max_change) % mod)

    def findMinDiff(self, helper, num):
        if num < helper[0]:
            return helper[0] - num
        if num > helper[-1]:
            return num - helper[-1]
        left, right = 0, len(helper)
        while right - left > 1:
            mid = left + (right - left) // 2
            if helper[mid] == num:
                return 0
            if helper[mid] > num:
                right = mid
            else:
                left = mid
        return min(num - helper[left], helper[right] - num)
