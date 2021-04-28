# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.dfs(root, str(root.val))
        return self.res
    
    def dfs(self, root, path):
        if not root.left and not root.right:
            self.res.append(path)
            return
        if root.left:
            self.dfs(root.left, path + "->" + str(root.left.val))
        if root.right:
            self.dfs(root.right, path + "->" + str(root.right.val))