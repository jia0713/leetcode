class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        inorder_stack, res, p = [], [], root
        while(True):
            if p != None:
                inorder_stack.append(p)
                p = p.left
            else:
                if not inorder_stack:
                    break
                p = inorder_stack[-1]
                res.append(p.val)
                p = p.right
                inorder_stack.pop()
        return res

#前序，中序，后序通用解法
class Solution_2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        p, istack, res = root, [], []
        while(p or istack):
            if not p:
                p = istack.pop()
                res.append(p.val)
                p = p.right
            else:
                if p.left == None:
                    res.append(p.val)
                    p = p.right
                else:
                    istack.append(p)
                    p = p.left
        return res



        