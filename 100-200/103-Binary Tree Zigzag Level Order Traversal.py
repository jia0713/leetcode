# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur, pre, res = [root], [], [[root.val]]
        count = 0
        while cur:
            pre = cur
            cur, temp_res = [], []
            for item in pre:
                if item.left:
                    cur.append(item.left)
                    temp_res.append(item.left.val)
                if item.right:
                    cur.append(item.right)
                    temp_res.append(item.right.val)
            if temp_res:
                if count % 2 == 0:
                    temp_res.reverse()
                res.append(temp_res)
            count += 1
        return res
