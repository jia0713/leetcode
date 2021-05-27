class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = list()
        if not nums or nums[0] * 4 > target or nums[-1] * 4 < target:
            return result
        nums_map = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] not in nums_map:
                    nums_map[nums[i] + nums[j]] = [[i, j]]
                else:
                    nums_map[nums[i] + nums[j]].append([i, j])

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                res_num = target - nums[i] - nums[j]
                if res_num not in nums_map:
                    continue
                else:
                    temp_list = nums_map[res_num]
                    for item in temp_list:
                        if item[0] > j and item[1] > j:
                            result.append(
                                [nums[i], nums[j]] + [nums[item[0]], nums[item[1]]]
                            )
                        else:
                            continue
        result = list(set(tuple(t) for t in result))
        return result
