class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        for i in range(len(str)):
            if str[i] != " ":
                break
        digit_dict = "0123456789"
        if str[i] not in digit_dict and str[i] != "+" and str[i] != "-":
            return 0
        if i == len(str) - 1:
            if str[i] == "+" or str[i] == "-":
                return 0
            else:
                return int(str[i])
        flag = 0
        str = str + " "
        if str[i] in digit_dict:
            flag = 1
            for j in range(i, len(str)):
                if str[j] not in digit_dict:
                    break
            digit_str = str[i:j]
        else:
            if str[i + 1] not in digit_dict:
                return 0
            if str[i] == "+":
                flag = 1
            if str[i] == "-":
                flag = -1
            for j in range(i + 1, len(str)):
                if str[j] not in digit_dict:
                    print(i, j)
                    break
            digit_str = str[i + 1 : j]
        intMax = pow(2, 31) - 1
        intMin = -1 * pow(2, 31)
        digit_sum = 0
        if flag == 1:
            for j in range(len(digit_str)):
                digit_sum += int(digit_str[j]) * pow(10, len(digit_str) - 1 - j)
                if digit_sum > intMax:
                    return intMax
            return digit_sum
        if flag == -1:
            for j in range(len(digit_str)):
                digit_sum += int(digit_str[j]) * pow(10, len(digit_str) - 1 - j)
                if -1 * digit_sum < intMin:
                    return intMin
            return -1 * digit_sum
