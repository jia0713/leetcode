class Solution:
    def plusOne(self, digits):
        for index in range(len(digits) - 1, 0, -1):
            digits[index] = (
                digits[index] + 1 if index == len(digits) - 1 else digits[index]
            )
            digits[index - 1] = digits[index - 1] + int(digits[index] / 10)
            digits[index] = digits[index] % 10
        if len(digits) == 1:
            digits[0] = digits[0] + 1
        if digits[0] == 10:
            return [1 if index == 0 else 0 for index in range(0, len(digits) + 1)]
        else:
            return digits

