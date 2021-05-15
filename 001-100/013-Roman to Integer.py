class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if not s:
            return 0
        # for i in range(len(s)):
        #     if s[i] not in roman_dict.keys():
        #         return 0
        if len(s) == 1:
            return roman_dict[s[0]]
        integer, pointer = 0, 0
        while pointer < len(s) - 1:
            if roman_dict[s[pointer]] >= roman_dict[s[pointer + 1]]:
                integer += roman_dict[s[pointer]]
                pointer += 1
            else:
                integer += roman_dict[s[pointer + 1]] - roman_dict[s[pointer]]
                pointer += 2
        if pointer == len(s) - 1:
            integer += roman_dict[s[pointer]]
        return integer


class Solution_2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 50, "X": 50, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for index, lett in enumerate(s):
            if index < len(s) - 1 and s[index : index + 2] in [
                "IV",
                "IX",
                "XL",
                "XC",
                "CD",
                "CM",
            ]:
                res -= roman[lett]
            else:
                res += roman[lett]
        return res