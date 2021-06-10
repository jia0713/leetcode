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
        if not root or root == p or root == q:
            return root
        # 函数的返回情况
        # 1，如果左或者右二叉树不存在p和q 返回空
        # 2. 如果左或者右二叉树同时存在p和q 这种情况和1必然同时发生 这棵树返回的是LCA
        # 3. p和q在左右二叉树一边一个，那么root就是想要的结果

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
