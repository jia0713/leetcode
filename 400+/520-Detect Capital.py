class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if self.isCapital(word[0]):
            for i in range(1, len(word)):
                if self.isCapital(word[i]) != self.isCapital(word[1]):
                    return False
        if not self.isCapital(word[0]):
            for i in range(1, len(word)):
                if self.isCapital(word[i]):
                    return False
        return True
                
    def isCapital(self, char):
        if ord(char) >= 97 and ord(char) <= 122:
            return False
        else:
            return True