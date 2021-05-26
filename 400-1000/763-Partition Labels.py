from collections import defaultdict


class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hash_table = defaultdict(int)
        for index, char in enumerate(s):
            hash_table[char] = index
        start, left = 0, 0
        res = []
        while start < len(s):
            right = hash_table[s[left]]
            while left <= right:
                right = max(right, hash_table[s[left]])
                left += 1
            res.append(right - start + 1)
            start, left = right + 1, right + 1
        return res


# 用一个数组和一个hash_table记录
# 稍微耗费空间
class Solution_2(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        hash_table, res = {}, []
        s_list = list(range(len(S)))
        for i, char in enumerate(S):
            if char not in hash_table:
                hash_table[char] = i
            else:
                s_list[hash_table[char] : (i + 1)] = [s_list[hash_table[char]]] * (
                    i + 1 - hash_table[char]
                )
        count, index, cur = 1, 1, s_list[0]
        while index < len(s_list):
            if s_list[index] == cur:
                count += 1
            else:
                res.append(count)
                cur = s_list[index]
                count = 1
            index += 1
        res.append(count)
        return res
