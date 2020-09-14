# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
    
    def helper(self, root):
        if not root:
            return 0, 0
        left_with, left_without = self.helper(root.left)
        right_with, right_without = self.helper(root.right)
        max_with = root.val + left_without + right_without
        max_without = max(left_with, left_without) + max(right_with, right_without)
        return max_with, max_without