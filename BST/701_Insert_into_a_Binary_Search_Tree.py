# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root == None:
            node = TreeNode(val)
            return node
        if root.val>val:
            root.left = self.insertIntoBST(root.left,val)
        elif root.val<val:
            root.right = self.insertIntoBST(root.right,val)
        return root
        