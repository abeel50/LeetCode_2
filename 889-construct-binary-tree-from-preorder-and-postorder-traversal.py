# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hash = {}
        for i,n in enumerate(postorder):
            hash[n] = i
        
        def helper(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return None
            
            root = TreeNode(preorder[i1])
            if i1 != i2:
                leftVal = preorder[i1 + 1]
                mid = hash[leftVal]
                leftSize = mid - j1 + 1
                root.left = helper(i1 + 1,i1 + leftSize,j1 ,mid)
                root.right = helper(i1 + leftSize + 1 ,i2 ,mid + 1,j2 - 1)
            return root
        
        return helper (0, len(postorder)-1 , 0, len(postorder)-1)  
