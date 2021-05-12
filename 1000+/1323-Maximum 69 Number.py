class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str, new_str = str(num), str(num)
        for i in range(len(num_str)):
            if num_str[i] == "6":
                new_str = num_str[:i] + "9" + num_str[i + 1 :]
                break
        return int(new_str)