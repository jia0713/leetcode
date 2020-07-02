class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            return ""
        rdict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        num_str = [0] * 4
        for i in range(4):
            num_str[3-i] = num % 10
            num = int(num / 10)
        roman_str = ""
        if num_str[0] != 0:
            roman_str += "M" * num_str[0]
        for i in range(1, 4):
            if num_str[i] != 0:
                key = ""
                if num_str[i] >=1 and num_str[i]<=3:
                    key = rdict[int(pow(10, 3-i))] * num_str[i]
                if num_str[i] == 4:
                    key = rdict[int(pow(10, 3-i))] + rdict[int(5 * pow(10, 3-i))]
                if num_str[i] >=5 and num_str[i]<=8:
                    key = rdict[int(5 * pow(10, 3-i))] + rdict[int(pow(10, 3-i))] * (num_str[i] - 5)
                if num_str[i] == 9:
                    key = rdict[int(pow(10, 3-i))] + rdict[int(pow(10, 4-i))]
                roman_str += key
        return roman_str