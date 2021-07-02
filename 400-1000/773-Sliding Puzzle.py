class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        board = board[0] + board[1]
        board = "".join([str(k) for k in board])
        res = self.oneMove(board)
        res, queue, visited = -1, [board], set()
        target = "123450"
        while queue:
            res += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr == target:
                    return res
                if curr in visited:
                    continue
                visited.add(curr)
                onemove = self.oneMove(curr)
                for item in onemove:
                    queue.append(item)
        return -1

    def oneMove(self, curr):
        onemove = []
        change_dict = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        index = 0
        for i in range(6):
            if curr[i] == "0":
                index = i
        for i in change_dict[index]:
            curr_copy = "".join(curr)
            temp = curr_copy[i]
            curr_copy = curr_copy.replace(temp, "0")
            curr_copy = curr_copy[0:index] + temp + curr_copy[index + 1 :]
            onemove.append(curr_copy)
        return onemove
