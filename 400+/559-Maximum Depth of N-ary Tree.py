"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        res, queue = 0, deque()
        queue.append(root)
        while queue:
            res += 1
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                children = node.children
                for child in children:
                    queue.append(child)
        return res
