class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if target == "0000":
            return 0
        deadends = set(deadends)
        res, queue = 0, ["0000"]
        while queue:
            res += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr in deadends:
                    continue
                onemove = self.oneMove(curr)
                deadends.add(curr)
                for item in onemove:
                    if item == target:
                        return res
                    queue.append(item)
        return -1

    def oneMove(self, curr):
        change_dict = {
            "0": ["1", "9"],
            "1": ["0", "2"],
            "2": ["1", "3"],
            "3": ["2", "4"],
            "4": ["3", "4"],
            "5": ["4", "6"],
            "6": ["5", "7"],
            "7": ["6", "8"],
            "8": ["7", "9"],
            "9": ["8", "0"],
        }
        onemove = []
        for index, char in enumerate(curr):
            for k in change_dict[char]:
                onemove.append(curr[0:index] + k + curr[index + 1:])
        return onemove
