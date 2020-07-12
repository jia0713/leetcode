class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        table_one = {}
        table_two = {}
        for index, letter in enumerate(pattern):
            if letter in table_one and table_one[letter] != str_list[index]:
                return False
            if str_list[index] in table_two and table_two[str_list[index]] != letter:
                return False
            table_one[letter] = str_list[index]
            table_two[str_list[index]] = letter
        return True