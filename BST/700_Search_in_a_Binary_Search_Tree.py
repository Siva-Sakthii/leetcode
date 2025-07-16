# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node = None
        def _searchBST(root,val):
            if root == None or root.val == val:
                return root
            elif root.val<val:
                return self.searchBST(root.right,val)
            elif root.val>val:
                return self.searchBST(root.left,val)
            return root
        return _searchBST(root,val)
        
    