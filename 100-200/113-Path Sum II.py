# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = []
        self.dfs(root, sum, [])
        return self.res
    
    def dfs(self, node, target, path):
    # 不能写path.append(node.val)
    # 原因是改变函数里的path,会继续传递到新的dfs参数中
        if not node.left and not node.right:
            if target == node.val:
                self.res.append(path + [node.val])
            return
        else:
            if node.left:
                self.dfs(node.left, target-node.val, path + [node.val])
            if node.right:
                self.dfs(node.right, target-node.val, path + [node.val])