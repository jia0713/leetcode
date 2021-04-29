# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        post_stack = [root]
        while post_stack:
            p = post_stack.pop()
            res = [p.val] + res
            if p.left:
                post_stack.append(p.left)
            if p.right:
                post_stack.append(p.right)
        return res


# 一个比较巧妙的方法
# 后续遍历 左-右-中，可以先写成前序遍历 中-右-左 然后把结果reverse
class Solution_2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        p, pstack, res = root, [], []
        while p or pstack:
            if p == None:
                p = pstack.pop()
                p = p.left
            else:
                pstack.append(p)
                res.append(p.val)
                p = p.right
        res.reverse()
        return res
