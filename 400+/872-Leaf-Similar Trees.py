# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = self.helper(root1, [])
        leaf2 = self.helper(root2, [])
        return leaf1 == leaf2

    def helper(self, root, path):
        if not root:
            return path
        if not root.left and not root.right:
            return path + [root.val]
        return self.helper(root.left, path) + self.helper(root.right, path)
