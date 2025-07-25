# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def _lca(root,p,q):
            if root == None:
                return None
            if p.val<root.val and q.val<root.val:
                return _lca(root.left,p,q)
            elif p.val>root.val and q.val>root.val:
                return _lca(root.right,p,q)
            return root
        return _lca(root,p,q)