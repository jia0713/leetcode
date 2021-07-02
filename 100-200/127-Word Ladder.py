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
                    new_word = cur_word[:i] + c + cur_word[i + 1:]
                    if new_word == endWord:
                        return cur_len + 1
                    if new_word in wordList:
                        queue.append((new_word, cur_len + 1))
                        wordList.remove(new_word)
        return 0


class Solution_2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        queue, res, visited = [beginWord], 1, set()
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                curr = queue.pop(0)
                for i in range(len(curr)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = curr[:i] + c + curr[i + 1:]
                        if new_word == endWord:
                            return res
                        if new_word in wordList:
                            if new_word in visited:
                                continue
                            queue.append(new_word)
                            visited.add(new_word)
        return 0
