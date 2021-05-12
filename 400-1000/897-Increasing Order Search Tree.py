# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left and (not root.right):
            return root
        res = []
        stack, node = [], root
        while(stack or node):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        root = TreeNode()
        p = root
        for i in range(len(res) - 1):
            p.val = res[i]
            p.right = TreeNode(res[i + 1])
            p = p.right
        return root