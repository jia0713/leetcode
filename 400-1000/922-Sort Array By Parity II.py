class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list, even_list = [], []
        for i in range(len(A) // 2):
            if A[2 * i] % 2 != 0:
                even_list.append(2 * i)
            if A[2 * i + 1] % 2 == 0:
                odd_list.append(2 * i + 1)
        for k in range(len(odd_list)):
            odd = odd_list[k]
            even = even_list[k]
            temp = A[odd]
            A[odd] = A[even]
            A[even] = temp
        return A