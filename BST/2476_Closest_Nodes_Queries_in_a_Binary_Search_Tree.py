# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        array = []
        def inorder(node,array):
            if node:
                inorder(node.left,array)
                array.append(node.val)
                inorder(node.right,array)
        inorder(root,array)
        
        def binarysearch(key,arr,ans):
            i = 0
            j = len(arr) - 1
            while i<=j:
                mid = (i+j)//2
                if arr[mid] == key:
                    break
                elif arr[mid] > key:
                    j = mid - 1 
                elif arr[mid] < key:
                    i = mid + 1
            if arr[mid] == key:
                ans.append([arr[mid],arr[mid]])
            elif arr[mid] > key:
                if mid-1>=0:
                    ans.append([arr[mid-1],arr[mid]])    
                else:
                    ans.append([-1,arr[mid]])     
            elif arr[mid]<key:
                if mid+1<len(arr):
                    ans.append([arr[mid],arr[mid+1]])
                else:
                    ans.append([arr[mid], -1])
        ans = []
        for q in queries:
            binarysearch(q,array,ans)
        return ans
                