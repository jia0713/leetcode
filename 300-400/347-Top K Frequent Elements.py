class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_table, res, max_freq, count = {}, [], 0, 0
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        max_freq = max(hash_table.values())
        bucket = [[] for _ in range(max_freq + 1)]
        for key, item in hash_table.items():
            bucket[item].append(key)
        for i in range(max_freq, -1, -1):
            if bucket[i]:
                res += bucket[i]
                count += len(bucket[i])
            if count == k:
                break
        return res
