# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 对于前序, 后续遍历，此种解法通用
# 前提是按照题目要求保证出栈顺序
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        p, res = root, []
        pstack = [root]
        while pstack:
            p = pstack.pop()
            res = res + [p.val]
            if p.right:
                pstack.append(p.right)
            if p.left:
                pstack.append(p.left)
        return res


# 解法二对前序，中序，后序遍历通用
class Solution_2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        p = root
        pstack, res = [], []
        while pstack or p:
            if not p:
                p = pstack.pop()
                p = p.right
            else:
                pstack.append(p)
                res.append(p.val)
                if p.left != None:
                    p = p.left
                else:
                    pstack.pop()
                    p = p.right
        return res
