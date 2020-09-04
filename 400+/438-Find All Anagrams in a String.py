class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        s_dict, p_dict = {}, {}
        for i in range(len(p)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if p[i] in p_dict:
                p_dict[p[i]] += 1
            else:
                p_dict[p[i]] = 1
        self.res = []
        self.isSameDict(s_dict, p_dict, 0)
        for index in range(0, len(s)-len(p)):
            new_add_index = len(p) + index
            if s[new_add_index] in s_dict:
                s_dict[s[new_add_index]] += 1
            else:
                s_dict[s[new_add_index]] = 1
            s_dict[s[index]] -= 1
            self.isSameDict(s_dict, p_dict, index + 1)
        return self.res
        
    def isSameDict(self, s_dict, p_dict, index):
        for key, value in p_dict.items():
            if key not in s_dict or s_dict[key] != value:
                return
        self.res.append(index)