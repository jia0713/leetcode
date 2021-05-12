class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # hash_table记录该字母最后一次出现的位置
        hash_table = {}
        for i, char in enumerate(S):
            hash_table[char] = i
        start, end, length, res = 0, 0, 1, []
        for i in range(len(S)):
            char = S[i]
            end = max(hash_table[char], end)
            length = end - start + 1
            if i == end:
                if i < len(S) - 1:
                    start, end = i + 1, hash_table[S[i + 1]]
                res.append(length)
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
