# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.node_x, self.node_y = None, None
        self.depth_x, self.depth_y = float("inf"), float("inf")
        self.dfs(root.left, root, 1, x, y)
        self.dfs(root.right, root, 1, x, y)
        return (self.node_x != self.node_y) and (self.depth_x == self.depth_y)

    def dfs(self, node, par, depth, x, y):
        if not node:
            return
        if node.val == x:
            self.node_x, self.depth_x = par, depth
        if node.val == y:
            self.node_y, self.depth_y = par, depth
        self.dfs(node.left, node, depth + 1, x, y)
        self.dfs(node.right, node, depth + 1, x, y)
