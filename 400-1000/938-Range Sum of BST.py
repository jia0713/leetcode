# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.res = 0
        self.findRangeSum(root, L, R)
        return self.res

    def findRangeSum(self, root, L, R):
        if not root:
            return
        if root.val >= L and root.val <= R:
            self.res += root.val
            self.findRangeSum(root.left, L, R)
            self.findRangeSum(root.right, L, R)
        if root.val < L:
            self.findRangeSum(root.right, L, R)
        if root.val > R:
            self.findRangeSum(root.left, L, R)