# c

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s, e = -1, -1
        l, u = 0, len(nums)
        if not nums or target > nums[u-1] or target < nums[l]:
            return [s, e]
        m = (l+u)//2
        while u > l:
            if nums[m] > target:
                u = m
                m = (l+u)//2
            elif nums[m] < target:
                l = m+1
                m = (l+u)//2
            else:
                s = e = m
                while 0 < s and nums[s-1] == nums[s]:
                    s-=1
                while e < len(nums)-1 and nums[e+1] == nums[e]:
                    e+=1
                break
        return [s, e]

if __name__ == '__main__':
    sol = Solution()
    answer = sol.searchRange([0, 3, 4], target=1)
    print (answer)



