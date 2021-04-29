# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        head_val = preorder[0]
        head_index = inorder.index(head_val)
        head = TreeNode(val=head_val)
        left_inorder, right_inorder = inorder[:head_index], inorder[(head_index + 1) :]
        left_length = len(left_inorder)
        left_preorder, right_preorder = (
            preorder[1 : (1 + left_length)],
            preorder[(1 + left_length) :],
        )
        head.left = self.buildTree(left_preorder, left_inorder)
        head.right = self.buildTree(right_preorder, right_inorder)
        return head


# 一个精简的多的写法，相同思想
# 这里不需要保证preorder和inorder的长度相同
class Solution_2(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1 :])
            return root
