"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            layer_root = root
            while(layer_root.left):
                cur = layer_root
                while(cur):
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                    cur = cur.next
                layer_root = layer_root.left
        return root