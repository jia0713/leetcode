# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if self.allZero(root):
            return
        if self.allZero(root.left):
            root.left = None
        if self.allZero(root.right):
            root.right = None
        self.pruneTree(root.left)
        self.pruneTree(root.right)
        return root
        
    def allZero(self, root):
        if not root:
            return True
        if root.val == 1:
            return False
        if root.val == 0 and not root.left and not root.right:
            return True
        return self.allZero(root.left) and self.allZero(root.right)
        
        
        