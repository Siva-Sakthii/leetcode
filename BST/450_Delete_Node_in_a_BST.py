# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def find_min(root):
            curr = root
            while curr.left:
                curr = curr.left
            return curr
        def _deleteNode(root,key):
            if root==None:
                return None
            
            if key>root.val:
                root.right = _deleteNode(root.right,key)
            elif key<root.val:
                root.left = _deleteNode(root.left,key)
            
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                
                else:
                    temp = find_min(root.right)
                    root.val = temp.val
                    root.right = _deleteNode(root.right,temp.val)
            return root


        root = _deleteNode(root,key)
        return root