class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l = max((sum(weights)-1) // D + 1, max(weights))
        r = sum(weights)
        while(l < r):
            candi, need = (l + r) // 2, 1
            remain = candi
            for i in range(len(weights)):
                if remain >= weights[i]:
                    remain -= weights[i]
                else:
                    need += 1
                    remain = candi - weights[i]
            if need > D:
                l = candi + 1
            if need <= D:
                r = candi
        return l