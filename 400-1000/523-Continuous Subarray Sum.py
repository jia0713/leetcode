class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = dict()
        counter[0], resi = -1, 0
        for index, num in enumerate(nums):
            resi = (resi + num) % k
            if resi in counter:
                if index - counter[resi] >= 2:
                    return True
            else:
                counter[resi] = index
        return False
