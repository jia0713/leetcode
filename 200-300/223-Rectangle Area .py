class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S1 = (C - A) * (D - B)
        S2 = (G - E) * (H - F)
        inter_a = max(min(C, G) - max(A, E), 0)
        inter_b = max(min(D, H) - max(B, F), 0)
        return S1 + S2 - inter_a * inter_b
