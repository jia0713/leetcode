# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res, queue = [], deque()
        queue.append([root])
        while(queue):
            cur_nodes = queue.popleft()
            res.append(cur_nodes[-1].val)
            new_nodes = []
            for node in cur_nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            if new_nodes:
                queue.append(new_nodes)
        return res