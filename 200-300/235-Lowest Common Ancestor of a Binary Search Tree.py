# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        small, big = min(p.val, q.val), max(p.val, q.val)
        res = root
        while(res.val > big or res.val < small):
            if res.val > big:
                res = res.left
            elif res.val < small:
                res = res.right
        return res