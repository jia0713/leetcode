class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        key_dict = {}
        for i, number in enumerate(numbers):
            if number in key_dict:
                return [key_dict[number] + 1, i + 1]
            if number <= target // 2:
                key_dict[target - number] = i


class Solution_2:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            if numbers[i] + numbers[j] < target:
                i = i + 1
            if numbers[i] + numbers[j] > target:
                j = j - 1
