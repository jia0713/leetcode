from collections import defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        counter = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                counter[stop].add(bus)
        res, queue = 0, [source]
        visited = [0] * 500
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                curr = queue.pop(0)
                for bus in counter[curr]:
                    if visited[bus]:
                        continue
                    visited[bus] = 1
                    for stop in routes[bus]:
                        if stop == target:
                            return res
                        queue.append(stop)
        return -1


if __name__ == "__main__":
    sol = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    source, target = 1, 6
    ans = sol.numBusesToDestination(routes, source, target)
    print(ans)
