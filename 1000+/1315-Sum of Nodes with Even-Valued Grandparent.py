# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        if root.val % 2 == 0:
            if root.left and root.left.left:
                self.res += root.left.left.val
            if root.left and root.left.right:
                self.res += root.left.right.val
            if root.right and root.right.left:
                self.res += root.right.left.val
            if root.right and root.right.right:
                self.res += root.right.right.val
        self.helper(root.left)
        self.helper(root.right)