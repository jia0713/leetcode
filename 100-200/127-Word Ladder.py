from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList = set(wordList) - set(beginWord)
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            cur_path = queue.popleft()
            cur_word, cur_len = cur_path[0], cur_path[1]
            for i in range(len(cur_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = cur_word[:i] + c + cur_word[i + 1 :]
                    if new_word == endWord:
                        return cur_len + 1
                    if new_word in wordList:
                        queue.append((new_word, cur_len + 1))
                        wordList.remove(new_word)
        return 0
