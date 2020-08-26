# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 这里的参数不能初始化到函数里面，所以只能在一开始初始化，这是一个要注意的技巧
class Solution(object):
    def isValidBST(self, root, min_value=float("-inf"), max_value=float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= min_value or root.val >= max_value:
            return False
        return self.isValidBST(root.left, min_value, root.val) and self.isValidBST(root.right, root.val, max_value)
        
        