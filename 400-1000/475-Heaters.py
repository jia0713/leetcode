class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        i = 1
        res = 0
        for house in houses:
            while i < len(heaters) - 1 and house > heaters[i]:
                i += 1
            res = max(res, min(heaters[i] - house, house - heaters[i - 1]))
        return res
