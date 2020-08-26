class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while(True):
            i, j = self.locatePointer(i, j, A)
            if i >= j:
                break
            A[i], A[j] = A[j], A[i]
        return A
    
    def locatePointer(self, i, j, A):
        while(i < len(A)):
            if A[i] % 2 == 0:
                i += 1
            else:
                break
        while(j >= 0):
            if A[j] % 2 != 0:
                j -= 1
            else:
                break
        return i, j
        