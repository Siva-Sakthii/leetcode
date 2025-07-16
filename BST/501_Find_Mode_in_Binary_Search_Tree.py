# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        max_count = 0
        modes = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nonlocal max_count, modes
            count[root.val] = 1+count.get(root.val,0)
            if count[root.val] > max_count:
                max_count = count[root.val]
                modes = [root.val]
            elif count[root.val] == max_count:
                modes.append(root.val)
            
            inorder(root.right)
        
        inorder(root)
        return modes
        