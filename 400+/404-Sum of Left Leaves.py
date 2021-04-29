# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root:
            return self.res
        self.calLeft(root.left, "left")
        self.calLeft(root.right, "right")
        return self.res

    def calLeft(self, root, label):
        if not root:
            return
        if not root.left and not root.right:
            if label == "left":
                self.res += root.val
        self.calLeft(root.left, "left")
        self.calLeft(root.right, "right")
