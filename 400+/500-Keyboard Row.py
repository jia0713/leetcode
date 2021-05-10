from collections import defaultdict


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        counter = defaultdict(int)
        for char in "qwertyuiopQWERTYUIOP":
            counter[char] = 0
        for char in "asdfghjklASDFGHJKL":
            counter[char] = 1
        for char in "zxcvbnmZXCVBNM":
            counter[char] = 2
        res = []
        for word in words:
            index = 1
            while index < len(word):
                if counter[word[index]] != counter[word[index - 1]]:
                    break
                index += 1
            if index == len(word):
                res.append(word)
        return res
