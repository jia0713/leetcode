class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_counter = {}
        for letter in magazine:
            if letter in mag_counter:
                mag_counter[letter] += 1
            else:
                mag_counter[letter] = 1
        for letter in ransomNote:
            if letter not in mag_counter or mag_counter[letter] <= 0:
                return False
            mag_counter[letter] -= 1
        return True
