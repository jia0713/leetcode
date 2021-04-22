# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        value = root.val
        return self.helper(root, value)
    
    def helper(self, root, value):
        if not root:
            return True
        if root.val != value:
            return False
        if not root.left and not root.right:
            return True
        return self.helper(root.left, value) and self.helper(root.right, value)