# 拓扑排序
from Queue import Queue
from collections import Counter


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree, graph = Counter(), {}
        count = 0
        for i in range(numCourses):
            graph[i] = []
        for pre in prerequisites:
            indegree[pre[1]] += 1
            graph[pre[0]] += [pre[1]]
        q = Queue()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.put(i)
        if q.empty():
            return False
        while not q.empty():
            cur = q.get()
            count += 1
            for item in graph[cur]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.put(item)
        if count == numCourses:
            return True
        else:
            return False
